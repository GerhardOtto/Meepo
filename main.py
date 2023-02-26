#use google auth for password
#diffie-hellman key exchange

import customtkinter
import tkinter
import encode
import emailer
from tkinter import filedialog

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root_width = 500
root_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (root_width // 2)
y = 100
root.geometry(f"{root_width}x{root_height}+{x}+{y}")

def closeProgram():
    exit()


def theFileExplorer():
    root = tkinter.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    return file_path

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

#Title
label = customtkinter.CTkLabel(master=frame, text="Lujvkl & Kljvkl", font=("Arial", 24))
label.pack(pady=12, padx=10)

#Dencode title
label = customtkinter.CTkLabel(master=frame, text="Dencode", font=("Arial", 24))
label.pack(pady=12, padx=10)
label.place(relx = 0.38, rely = 0.6)

#Ecode title
label = customtkinter.CTkLabel(master=frame, text="Encode", font=("Arial", 24))
label.pack(pady=12, padx=10)
label.place(relx = 0.4, rely = 0.4)

#fileExplorer button
button = customtkinter.CTkButton(master=frame, text="FileExplorer", command=theFileExplorer)
button.pack(pady=12, padx=10)
button.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

#close button
button = customtkinter.CTkButton(master=frame, text="Close", command=closeProgram,width=120,height=32,border_width=1,corner_radius=8)
button.pack(pady=12, padx = 10)
button.place(relx=0.8, rely=0.95, anchor=tkinter.CENTER)

def email():
    dialog = customtkinter.CTkInputDialog(text="Enter Email address:", title="Send Mail")
    dialog_width = dialog.winfo_reqwidth()
    dialog_height = dialog.winfo_reqheight()
    root.update_idletasks()  # update the root window to get the correct values for its dimensions
    root_width = root.winfo_width()
    root_height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (dialog_width // 2)
    y = (root.winfo_screenheight() // 2) - (dialog_height // 2) - (root_height // 2)
    dialog.geometry(f"{dialog_width}x{dialog_height}+{x}+{y}")
    emailaddress = dialog.get_input()
    emailer.send_mail(emailaddress)


#email button
button = customtkinter.CTkButton(master=frame, text="Email", command=email,width=120,height=32,border_width=1,corner_radius=8)
button.pack(pady=12, padx = 10)
button.place(relx=0.2, rely=0.95, anchor=tkinter.CENTER)

#progress bar
#progressbar = customtkinter.CTkProgressBar(master=frame,width=160,height=20,border_width=5, indeterminate_speed=True)
#progressbar.place(relx=0.5, rely=0.82, anchor=tkinter.CENTER)
#progressbar.set(0)

#segmented button for encoding
def segmented_button_callback(value):
    if (value == "Encode 1"):
        print("First button clicked")
    if (value == "Encode 2"):
        print("Seccond button clicked")
    if (value == "Encode 3"):
        print("Third button clicked")
    if (value == "Encode 4"):
        print("Fourth button clicked")
        
    segemented_buttonEncoder.set("Value 0")

segemented_buttonEncoder = customtkinter.CTkSegmentedButton(master=frame,values=["Encode 1", "Encode 2", "Encode 3", "Encode 4"],command=segmented_button_callback)
segemented_buttonEncoder.pack(padx=20, pady=10)
segemented_buttonEncoder.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

#segmented button for decoding
def segmented_button_callback(value):
    if (value == "Decode 1"):
        print("First button clicked")
    if (value == "Decode 2"):
        print("Seccond button clicked")
    if (value == "Decode 3"):
        print("Third button clicked")
    if (value == "Decode 4"):
        print("Fourth button clicked")

    segemented_buttonDecoder.set("Value 5")

segemented_buttonDecoder = customtkinter.CTkSegmentedButton(master=frame,values=["Decode 1", "Decode 2", "Decode 3", "Decode 4"],command=segmented_button_callback)
segemented_buttonDecoder.pack(padx=20, pady=10)
segemented_buttonDecoder.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

#input dialog
def button_click_event():
    dialog = customtkinter.CTkInputDialog(text="Type in a custom key:", title="Custom Key")
    dialog_width = dialog.winfo_reqwidth()
    dialog_height = dialog.winfo_reqheight()
    root.update_idletasks()  # update the root window to get the correct values for its dimensions
    root_width = root.winfo_width()
    root_height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (dialog_width // 2)
    y = (root.winfo_screenheight() // 2) - (dialog_height // 2) - (root_height // 2)
    dialog.geometry(f"{dialog_width}x{dialog_height}+{x}+{y}")
    print("Password:", dialog.get_input())


button = customtkinter.CTkButton(root, text="Custom Key", command=button_click_event)
button.pack(pady=12, padx = 10)
button.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

root.mainloop()
