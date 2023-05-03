import customtkinter
import tkinter
import endec
import emailer
import fileExplorer
import binary
import readWrite
import aes
import rsa

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

#decode title
labelDecode = customtkinter.CTkLabel(master=frame, text="Decode", font=("Arial", 24))
labelDecode.pack(pady=12, padx=10)
labelDecode.place(relx = 0.38, rely = 0.6)

#encode title
labelEncode = customtkinter.CTkLabel(master=frame, text="Encode", font=("Arial", 24))
labelEncode.pack(pady=12, padx=10)
labelEncode.place(relx = 0.4, rely = 0.4)

#fileExplorer button
filePath = None
def clickFileExplorer():
    global filePath
    filePath = fileExplorer.theFileExplorer(filePath)


buttonExplore = customtkinter.CTkButton(master=frame, text="FileExplorer", command=clickFileExplorer)
buttonExplore.pack(pady=12, padx=10)
buttonExplore.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

#close button
def closeProgram():
    exit()


buttonExit = customtkinter.CTkButton(master=frame, text="Close", command=closeProgram,width=120,height=32,border_width=1,corner_radius=8)
buttonExit.pack(pady=12, padx = 10)
buttonExit.place(relx=0.8, rely=0.95, anchor=tkinter.CENTER)

#email button
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
    binary.encodeToBinary(filePath)
    if emailAddress != None:
        emailer.sendMail(emailAddress,filePath)


buttonEmail = customtkinter.CTkButton(master=frame, text="Email", command=email,width=120,height=32,border_width=1,corner_radius=8)
buttonEmail.pack(pady=12, padx = 10)
buttonEmail.place(relx=0.2, rely=0.95, anchor=tkinter.CENTER)

#popup button
def popup(value):
    popup = tkinter.Toplevel()
    popup.title("Button Clicked")

    # Remove minimize and close buttons from the popup window
    popup.overrideredirect(True)

    message = "Button clicked: " + value
    tkinter.Label(popup, text=message, bg="#303030", fg="white").pack()

    # Add an "Okay" button to the popup window
    button_okay = tkinter.Button(popup, text="Okay", command=popup.destroy, bg="#505050", fg="white")
    button_okay.pack(pady=10)

    # Set the background color of the popup window
    popup.configure(bg="#303030")

    # Get the dimensions and position of the root window
    root_width = root.winfo_width()
    root_height = root.winfo_height()
    root_x = root.winfo_x()
    root_y = root.winfo_y()

    # Calculate the center position of the root window
    center_x = root_x + int(root_width / 2)
    center_y = root_y + int(root_height / 2)

    # Get the dimensions of the popup window
    popup_width = popup.winfo_width()
    popup_height = popup.winfo_height()

    # Calculate the position of the popup window relative to the center position of the root window
    popup_x = center_x - int(popup_width / 2) - 75
    popup_y = center_y - int(popup_height / 2)

    # Position the popup window
    popup.geometry(f"+{popup_x}+{popup_y}")

    popup.focus_set()
    popup.grab_set()
    popup.wait_window()


#segmented button for encrypting
def clickSegmentedButtonEncode(value):
    global hashedPassword
    global normalPassword

    if (value == "Encode OwnAlgo"):
        if (hashedPassword == None):
            hashedPassword = "NULL"
    
        print("Now starting encrypting with own algo...")
        readWrite.encodeWithOwnAlgo(filePath,hashedPassword)
        readWrite.deleteFile(filePath)
        print("Done!")


    elif value == "AES Encode":
        if (normalPassword == None):
            normalPassword = "NULL"
        
        print("Now starting encrypting with AES...")
        salt = aes.generateSalt()
        with open("salt.salt", "wb") as salt_file:
            salt_file.write(salt)
        key = aes.generateKey(normalPassword, oldSalt=True)
        aes.encrypt(filePath, key)
        print("Done!")

    
    elif value == "RSA Encode":
        if (hashedPassword == None):
            hashedPassword = endec.hashSlingingSlasher("NULL")

        print("Now starting encrypting with RSA...")
        public = rsa.generatePublicPrimesFromPassword(hashedPassword)
        rsa.writeRSAEncrypted(filePath,public)
        print("Done!")


    popup(value) 
    segementedButtonEncoder.set("null")


segementedButtonEncoder = customtkinter.CTkSegmentedButton(master=frame,values=["AES Encode", "Encode OwnAlgo", "RSA Encode"],command=clickSegmentedButtonEncode)
segementedButtonEncoder.pack(padx=20, pady=10)
segementedButtonEncoder.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

#segmented button for decrypting
def clickSegmentedButtonDecode(value):
    global hashedPassword
    global normalPassword

    if (value == "Decode OwnAlgo"):
        if (hashedPassword == None):
            hashedPassword = "NULL"

        print("Now starting decrypting with own algo...")
        readWrite.decodeWithOwnAlgo(filePath,hashedPassword)
        readWrite.deleteFile(filePath)
        print("Done!")


    elif value == "AES Decode":
        if (normalPassword == None):
            normalPassword = "NULL"

        print("Now starting decrypting with AES...")
        aes.loadSalt()
        key = aes.generateKey(normalPassword, oldSalt=True)
        aes.decrypt(filePath, key)
        print("Done!")


    elif value == "RSA Decode":
        if (hashedPassword == None):
            hashedPassword = endec.hashSlingingSlasher("NULL")

        print("Now starting decrypting with RSA...")
        public = rsa.generatePublicPrimesFromPassword(hashedPassword)
        private = rsa.generatePrivatePrimesFromPassword(public)
        rsa.writeRSADecrypted(filePath,private)
        print("Done!")


    popup(value)
    segementedButtonDecoder.set("null")


segementedButtonDecoder = customtkinter.CTkSegmentedButton(master=frame,values=["AES Decode", "Decode OwnAlgo", "RSA Decode"],command=clickSegmentedButtonDecode)
segementedButtonDecoder.pack(padx=20, pady=10)
segementedButtonDecoder.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

#password
hashedPassword = None
normalPassword = None
def clickPassword():
    global hashedPassword
    global normalPassword
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
    normalPassword = password
    hashedPassword = endec.hashSlingingSlasher(password)


buttonPassword = customtkinter.CTkButton(root, text="Enter Password", command=clickPassword)
buttonPassword.pack(pady=12, padx = 10)
buttonPassword.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

root.mainloop()