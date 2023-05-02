import customtkinter
import tkinter
import endec
import emailer
import fileExplorer
import binary
import readWrite
import aes

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

#segmented button for encoding
def clickSegmentedButtonEncode(value):

    if (value == "Encode OwnAlgo"):
        print("Now starting encoding with own algo...")
        readWrite.encodeWithOwnAlgo(filePath,hashedPassword)
        readWrite.deleteFile(filePath)
        print("Done!")

    elif value == "AES Encode":
        print("Now starting encoding with AES...")
        # Generate a new salt and save it to a file
        salt = aes.generate_salt()
        with open("salt.salt", "wb") as salt_file:
            salt_file.write(salt)
        # Generate the key using the password and salt
        key = aes.generate_key(normalPassword, load_existing_salt=True)
         # Encrypt the file
        aes.encrypt(filePath, key)
        print("Done!")

        
    segementedButtonEncoder.set("null")


segementedButtonEncoder = customtkinter.CTkSegmentedButton(master=frame,values=["AES Encode", "Encode OwnAlgo"],command=clickSegmentedButtonEncode)
segementedButtonEncoder.pack(padx=20, pady=10)
segementedButtonEncoder.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

#segmented button for decoding
def clickSegmentedButtonDecode(value):

    if (value == "Decode OwnAlgo"):
        print("Now starting decoding with own algo...")
        readWrite.decodeWithOwnAlgo(filePath,hashedPassword)
        print("Done!")


    elif value == "AES Decode":
        print("Now starting decoding with AES...")
        salt = aes.load_salt()
        key = aes.generate_key(normalPassword, load_existing_salt=True)
        aes.decrypt(filePath, key)
        print("Done!")

    segementedButtonDecoder.set("null")


segementedButtonDecoder = customtkinter.CTkSegmentedButton(master=frame,values=["AES Decode", "Decode OwnAlgo"],command=clickSegmentedButtonDecode)
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