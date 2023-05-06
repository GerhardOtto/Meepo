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

#Decode title
labelDecode = customtkinter.CTkLabel(master=frame, text="Decode", font=("Arial", 24))
labelDecode.pack(pady=12, padx=10)
labelDecode.place(relx = 0.38, rely = 0.6)

#Encode title
labelEncode = customtkinter.CTkLabel(master=frame, text="Encode", font=("Arial", 24))
labelEncode.pack(pady=12, padx=10)
labelEncode.place(relx = 0.4, rely = 0.4)

#FileExplorer button
filePath = None
def clickFileExplorer():
    global filePath
    filePath = fileExplorer.theFileExplorer(filePath)


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
    emailer.encodeToBinary(filePath)
    if emailAddress != None:
        emailer.sendMail(emailAddress,filePath)
        popup("Mail Sent!")


buttonEmail = customtkinter.CTkButton(master=frame, text="Email", command=email,width=120,height=32,border_width=1,corner_radius=8)
buttonEmail.pack(pady=12, padx = 10)
buttonEmail.place(relx=0.2, rely=0.95, anchor=tkinter.CENTER)

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
def clickSegmentedButtonEncode(value):
    global hashedPassword

    if (value == "Encode OwnAlgo"):
        if (hashedPassword == None):
            hashedPassword = "NULL"
    
        print("Now starting encrypting with own algo...")
        handelPW.savePassword(hashedPassword,filePath)
        readWrite.encodeWithOwnAlgo(filePath,hashedPassword)
        readWrite.deleteFile(filePath)
        print("Done!")
    
    elif value == "RSA Encode":
        if (hashedPassword == None):
            hashedPassword = endec.hashSlingingSlasher("NULL")

        print("Now starting encrypting with RSA...")
        publicKey, privateKey = rsa.generate_rsa_keys(32)
        rsa.store_keys(hashedPassword, publicKey, privateKey)
        rsa.encrypt_file(filePath, publicKey)
        readWrite.deleteFile(filePath)
        print("Done!")


    popup("Button clicked: " + value) 
    segementedButtonEncoder.set("null")


segementedButtonEncoder = customtkinter.CTkSegmentedButton(master=frame,values=["Encode OwnAlgo", "RSA Encode"],command=clickSegmentedButtonEncode)
segementedButtonEncoder.pack(padx=20, pady=10)
segementedButtonEncoder.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

#Segmented button for decrypting
def clickSegmentedButtonDecode(value):
    global hashedPassword

    if (value == "Decode OwnAlgo"):
        if (hashedPassword == None):
            hashedPassword = "NULL"

        print("Now starting decrypting with own algo...")
        newfilePath, fileData = readWrite.decodeWithOwnAlgo(filePath,hashedPassword)
        
        with open(newfilePath, "wb") as file:
            file.write(fileData)


        if handelPW.comparePassword(hashedPassword,newfilePath):
                readWrite.deleteFile(filePath)
                popup("Password is correct, OwnAlgo decrypted!")
        else:
            popup("Password is incorrect!")


        print("Done!")


    elif value == "RSA Decode":
        if (hashedPassword == None):
            hashedPassword = endec.hashSlingingSlasher("NULL")

        try:
            print("Now starting encrypting with RSA...")
            privateKey = rsa.getPrivateKey(hashedPassword)
            
            if (privateKey is not None):
                rsa.decrypt_file(filePath, privateKey)
                readWrite.deleteFile(filePath)
                popup("Password is correct, RSA decrypted!")
            else:
                popup("Password is incorrect!")

            print("Done!")
        except Exception as e:
            print("Error occurred: ", e)

    segementedButtonDecoder.set("null")


segementedButtonDecoder = customtkinter.CTkSegmentedButton(master=frame,values=["Decode OwnAlgo", "RSA Decode"],command=clickSegmentedButtonDecode)
segementedButtonDecoder.pack(padx=20, pady=10)
segementedButtonDecoder.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

#Password
hashedPassword = None

def clickPassword():
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


buttonPassword = customtkinter.CTkButton(root, text="Enter Password", command=clickPassword, width=25)
buttonPassword.pack(pady=12, padx=10)
buttonPassword.place(relx=0.365, rely=0.35, anchor=tkinter.CENTER)


def createPassowrd():
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
    handelPW.savePassword(hashedPassword, filePath)


buttonCreaetePassword = customtkinter.CTkButton(root, text="Create Password", command=createPassowrd, width=25)
buttonCreaetePassword.pack(pady=12, padx=10)
buttonCreaetePassword.place(relx=0.625, rely=0.35, anchor=tkinter.CENTER)



root.mainloop()