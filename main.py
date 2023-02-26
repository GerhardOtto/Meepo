#use google auth for password
import customtkinter
import tkinter
import encode

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("500x500")

def closeProgram():
    exit()


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="File Encoder", font=("Arial", 24))
label.pack(pady=12, padx=10)

#text boxes
#entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Text")
#entry1.pack(pady=12, padx=10)
#entry = customtkinter.CTkEntry(master=frame,width=320,height=100,corner_radius=10, placeholder_text="Hello")
#entry.place(relx=0.5, rely=0.5)

#close button
button = customtkinter.CTkButton(master=frame, text="Close", command=closeProgram,width=120,height=32,border_width=1,corner_radius=8)
button.pack(pady=12, padx = 10)
button.place(relx=0.8, rely=0.95, anchor=tkinter.CENTER)

#run button
button = customtkinter.CTkButton(master=frame, text="Run", command=encode.ownAlgoEncoder,width=120,height=32,border_width=1,corner_radius=8)
button.pack(pady=12, padx = 10)
button.place(relx=0.2, rely=0.95, anchor=tkinter.CENTER)

#progress bar
progressbar = customtkinter.CTkProgressBar(master=frame,width=160,height=20,border_width=5)
progressbar.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
progressbar.set(0.1)

#segmented button
def segmented_button_callback(value):
    if (value == "Value 1"):
        print("First button clicked")
        segemented_button.set("Value 5")
    if (value == "Value 2"):
        print("Seccond button clicked")
        segemented_button.set("Value 5")
    if (value == "Value 3"):
        print("Third button clicked")
        segemented_button.set("Value 5")
    if (value == "Value 4"):
        print("Fourth button clicked")
        segemented_button.set("Value 5")

segemented_button = customtkinter.CTkSegmentedButton(master=frame,values=["Value 1", "Value 2", "Value 3", "Value 4"],command=segmented_button_callback)
segemented_button.pack(padx=20, pady=10)
segemented_button.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

#input dialog
def button_click_event():
    dialog = customtkinter.CTkInputDialog(text="Type in a key:", title="Custom Key")
    print("Password:", dialog.get_input())


button = customtkinter.CTkButton(root, text="Custom Key", command=button_click_event)
button.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

root.mainloop()
