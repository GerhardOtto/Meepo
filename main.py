#use google auth for password
#diffie-hellman key exchange

import customtkinter
import tkinter
import endec
import emailer
import fileExplorer
import base64Manip
import readWrite

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
labelDecode = customtkinter.CTkLabel(master=frame, text="Dencode", font=("Arial", 24))
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
    base64Manip.touchBase()
    if emailAddress != None:
        emailer.sendMail(emailAddress)


buttonEmail = customtkinter.CTkButton(master=frame, text="Email", command=email,width=120,height=32,border_width=1,corner_radius=8)
buttonEmail.pack(pady=12, padx = 10)
buttonEmail.place(relx=0.2, rely=0.95, anchor=tkinter.CENTER)

#segmented button for encoding
encodedString = None
def clickSegmentedButtonEncode(value):
    global encodedString
    fileToBase64 = base64Manip.touchBase(filePath)
    if (value == "Encode 1"):
        encodedString = endec.rsaAlgoEncoder(fileToBase64,hashedPassword)
        readWrite.write(encodedString,hashedPassword)
        print(encodedString + " not done yet!")
    if (value == "Encode OwnAlg"):
        encodedString = endec.ownAlgoEncoder(fileToBase64,hashedPassword)
        print(encodedString)
        
    segementedButtonEncoder.set("null")


segementedButtonEncoder = customtkinter.CTkSegmentedButton(master=frame,values=["Encode 1", "Encode OwnAlg"],command=clickSegmentedButtonEncode)
segementedButtonEncoder.pack(padx=20, pady=10)
segementedButtonEncoder.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

#segmented button for decoding
def clickSegmentedButtonDecode(value):
    if (value == "Decode 1"):
        print("First button clicked")
        encodedText = readWrite.read(hashedPassword,filePath)
        decodedText = endec.rsaAlgoDecoder(encodedText)
        base64Text = base64Manip.leaveBase(decodedText)
    if (value == "Decode OwnAlgo"):
        print("Seccond button clicked")
        base64Text = base64Manip.leaveBase(filePath)

    segementedButtonDecoder.set("null")

    return base64Text


segementedButtonDecoder = customtkinter.CTkSegmentedButton(master=frame,values=["Decode 1", "Decode OwnAlgo"],command=clickSegmentedButtonDecode)
segementedButtonDecoder.pack(padx=20, pady=10)
segementedButtonDecoder.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

#password
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
    #print("Password:", dialog.get_input())


buttonPassword = customtkinter.CTkButton(root, text="Enter Password", command=clickPassword)
buttonPassword.pack(pady=12, padx = 10)
buttonPassword.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

root.mainloop()
