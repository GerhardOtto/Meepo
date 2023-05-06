import customtkinter
import tkinter
import endec
import emailer
import fileExplorer
import readWrite
import rsa
import handelPW


customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
rootWidth = 500
rootHeight = 500
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
x = (screenWidth // 2) - (rootWidth // 2)
y = 100
root.geometry(f"{rootWidth}x{rootHeight}+{x}+{y}")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

#Title
labelTitle = customtkinter.CTkLabel(master=frame, text="ENDEC", font=("Arial", 24))
labelTitle.pack(pady=12, padx=10)

#Decrypt title
labelDecrypt = customtkinter.CTkLabel(master=frame, text="Decrypt", font=("Arial", 24))
labelDecrypt.pack(pady=12, padx=10)
labelDecrypt.place(relx = 0.38, rely = 0.6)

#Encrypt title
labelEncrypt = customtkinter.CTkLabel(master=frame, text="Encrypt", font=("Arial", 24))
labelEncrypt.pack(pady=12, padx=10)
labelEncrypt.place(relx = 0.4, rely = 0.4)

#FileExplorer button
filePath = None
def clickFileExplorer():
    global filePath
    filePath = fileExplorer.theFileExplorer(filePath)
    buttonCreateEncrypt.configure(state=tkinter.NORMAL)
    buttonCreateDecrypt.configure(state=tkinter.NORMAL)
    buttonEmail.configure(state=tkinter.NORMAL)

buttonExplore = customtkinter.CTkButton(master=frame, text="FileExplorer", command=clickFileExplorer, width=240)
buttonExplore.pack(pady=12, padx=10)
buttonExplore.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

#Close button
def closeProgram():
    exit()


buttonExit = customtkinter.CTkButton(master=frame, text="Close", command=closeProgram,width=120,height=32,border_width=1,corner_radius=8)
buttonExit.pack(pady=12, padx = 10)
buttonExit.place(relx=0.8, rely=0.95, anchor=tkinter.CENTER)

#Email button
def email():
    dialog = customtkinter.CTkInputDialog(text="Enter Email address:", title="Send Mail")
    dialogWidth = dialog.winfo_reqwidth()
    dialogHeight = dialog.winfo_reqheight()
    root.update_idletasks()  # update the root window to get the correct values for its dimensions
    rootHeight = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (dialogWidth // 2)
    y = (root.winfo_screenheight() // 2) - (dialogHeight // 2) - (rootHeight // 2)
    dialog.geometry(f"{dialogWidth}x{dialogHeight}+{x}+{y}")
    emailAddress = dialog.get_input()
    emailer.EncryptToBinary(filePath)
    if emailAddress != None:
        emailer.sendMail(emailAddress,filePath)
        popup("Mail Sent!")
        buttonEmail.configure(state=tkinter.DISABLED)


buttonEmail = customtkinter.CTkButton(master=frame, text="Email", command=email,width=120,height=32,border_width=1,corner_radius=8)
buttonEmail.pack(pady=12, padx = 10)
buttonEmail.place(relx=0.2, rely=0.95, anchor=tkinter.CENTER)
buttonEmail.configure(state=tkinter.DISABLED)

#Popup button
def popup(theMessage):
    popup = tkinter.Toplevel()
    popup.title("Button Clicked")
    popup.overrideredirect(True)

    message = theMessage
    tkinter.Label(popup, text=message, bg="#303030", fg="white").pack()

    button_okay = tkinter.Button(popup, text="Okay", command=popup.destroy, bg="#505050")
    button_okay.pack(pady=10)

    popup.configure(bg="#303030")

    root_width = root.winfo_width()
    root_height = root.winfo_height()
    root_x = root.winfo_x()
    root_y = root.winfo_y()

    center_x = root_x + int(root_width / 2)
    center_y = root_y + int(root_height / 2)

    popup_width = popup.winfo_width()
    popup_height = popup.winfo_height()

    popup_x = center_x - int(popup_width / 2) - 75
    popup_y = center_y - int(popup_height / 2)

    popup.geometry(f"+{popup_x}+{popup_y}")

    popup.focus_set()
    popup.grab_set()
    popup.wait_window()


#Segmented button for encrypting
def clickSegmentedButtonEncrypt(value):
    global hashedPassword

    if (value == "Encrypt OwnAlgo"):
        if (hashedPassword == None):
            hashedPassword = "NULL"
    
        print("Now starting encrypting with own algo...")
        handelPW.savePassword(hashedPassword,filePath)
        readWrite.encryptWithOwnAlgo(filePath,hashedPassword)
        readWrite.deleteFile(filePath)
        print("Done!")
    
    elif value == "RSA Encrypt":
        if (hashedPassword == None):
            hashedPassword = endec.hashSlingingSlasher("NULL")

        print("Now starting encrypting with RSA...")
        publicKey, privateKey = rsa.generateRsaKeys(32)
        binary = rsa.encryptFile(filePath, publicKey)
        rsa.storeKeys(binary, hashedPassword, publicKey, privateKey)
        readWrite.deleteFile(filePath)
        print("Done!")


    popup("Button clicked: " + value) 
    segementedButtonEncryptr.set("null")
    segementedButtonEncryptr.configure(state = "disabled")


segementedButtonEncryptr = customtkinter.CTkSegmentedButton(master=frame,values=["Encrypt OwnAlgo", "RSA Encrypt"],command=clickSegmentedButtonEncrypt)
segementedButtonEncryptr.pack(padx=20, pady=10)
segementedButtonEncryptr.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
segementedButtonEncryptr.configure(state = "disabled")

#Segmented button for decrypting
def clickSegmentedButtonDecrypt(value):
    global hashedPassword

    if (value == "Decrypt OwnAlgo"):
        if (hashedPassword == None):
            hashedPassword = "NULL"

        print("Now starting decrypting with own algo...")
        newfilePath, fileData = readWrite.decryptWithOwnAlgo(filePath,hashedPassword)
        
        with open(newfilePath, "wb") as file:
            file.write(fileData)


        if handelPW.comparePassword(hashedPassword,newfilePath):
                readWrite.deleteFile(filePath)
                popup("Password is correct, OwnAlgo decrypted!")
        else:
            popup("Password is incorrect!")


        print("Done!")


    elif value == "RSA Decrypt":
        if (hashedPassword == None):
            hashedPassword = endec.hashSlingingSlasher("NULL")

        try:
            print("Now starting encrypting with RSA...")
            binary, privateKey = rsa.getPrivateKey(hashedPassword)
            
            if ((binary == handelPW.readBinary(filePath) and privateKey is not None) or hashedPassword == endec.hashSlingingSlasher("NULL")):
                rsa.decryptFile(filePath, privateKey)
                readWrite.deleteFile(filePath)
                popup("Password is correct, RSA decrypted!")
            else:
                popup("Password is incorrect!")

            print("Done!")
        except Exception as e:
            print("Error occurred: ", e)

    segementedButtonDecrypt.set("null")
    segementedButtonDecrypt.configure(state = "disabled")


segementedButtonDecrypt = customtkinter.CTkSegmentedButton(master=frame,values=["Decrypt OwnAlgo", "RSA Decrypt"],command=clickSegmentedButtonDecrypt)
segementedButtonDecrypt.pack(padx=20, pady=10)
segementedButtonDecrypt.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)
segementedButtonDecrypt.configure(state = "disabled")

#Password
hashedPassword = None

def clickDecrypt():
    global hashedPassword
    dialog = customtkinter.CTkInputDialog(text="Type in a password:", title="Password")
    dialogWidth = dialog.winfo_reqwidth()
    dialogHeight = dialog.winfo_reqheight()
    root.update_idletasks()  # update the root window to get the correct values for its dimensions
    rootWidth = root.winfo_width()
    rootHeight = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (dialogWidth // 2)
    y = (root.winfo_screenheight() // 2) - (dialogHeight // 2) - (rootHeight // 2)
    dialog.geometry(f"{dialogWidth}x{dialogHeight}+{x}+{y}")
    password = dialog.get_input()
    hashedPassword = endec.hashSlingingSlasher(password)
    segementedButtonDecrypt.configure(state = "enabled")


buttonCreateDecrypt = customtkinter.CTkButton(root, text="Start Decrypting", command=clickDecrypt, width=25)
buttonCreateDecrypt.pack(pady=12, padx=10)
buttonCreateDecrypt.place(relx=0.625, rely=0.35, anchor=tkinter.CENTER)
buttonCreateDecrypt.configure(state=tkinter.DISABLED)


def clickEncrypt():
    global hashedPassword
    dialog = customtkinter.CTkInputDialog(text="Type in a password:", title="Password")
    dialogWidth = dialog.winfo_reqwidth()
    dialogHeight = dialog.winfo_reqheight()
    root.update_idletasks()  # update the root window to get the correct values for its dimensions
    rootWidth = root.winfo_width()
    rootHeight = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (dialogWidth // 2)
    y = (root.winfo_screenheight() // 2) - (dialogHeight // 2) - (rootHeight // 2)
    dialog.geometry(f"{dialogWidth}x{dialogHeight}+{x}+{y}")
    password = dialog.get_input()
    hashedPassword = endec.hashSlingingSlasher(password)
    segementedButtonEncryptr.configure(state = "enabled")
    


buttonCreateEncrypt = customtkinter.CTkButton(root, text="Start Encrypting", command=clickEncrypt, width=25)
buttonCreateEncrypt.pack(pady=12, padx=10)
buttonCreateEncrypt.place(relx=0.365, rely=0.35, anchor=tkinter.CENTER)
buttonCreateEncrypt.configure(state=tkinter.DISABLED)

root.mainloop()