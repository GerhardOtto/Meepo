#use google auth for password
import customtkinter
import tkinter
import encode

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("1080x720")

def closeProgram():
    exit()


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="File Encoder", font=("Arial", 24))
label.pack(pady=12, padx=10)

#text boxes
entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Text")
entry1.pack(pady=12, padx=10)
entry = customtkinter.CTkEntry(master=frame,width=320,height=100,corner_radius=10, placeholder_text="Hello")
entry.place(relx=0.5, rely=0.5)

#close button
button = customtkinter.CTkButton(master=frame, text="Close", command=closeProgram)
button.pack(pady=12, padx = 10)
button.place(relx=0.9, rely=0.95, anchor=tkinter.CENTER)

#run button
button = customtkinter.CTkButton(master=frame, text="Run", command=encode.ownAlgoEncoder,width=120,height=32,border_width=1,corner_radius=8)
button.pack(pady=12, padx = 12)
button.place(relx=0.1, rely=0.95, anchor=tkinter.CENTER)

#progress bar
progressbar = customtkinter.CTkProgressBar(master=frame,width=160,height=20,border_width=5)
progressbar.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
progressbar.set(0.1)

#radio button
def print_var(*args):
    xdLOL = radiobutton_var.get()
    print(xdLOL)


radiobutton_var = tkinter.IntVar(value=1)
radiobutton_1 = customtkinter.CTkRadioButton(master=root, text= "Test", variable=radiobutton_var, value=1, bg_color="transparent",border_width_checked=7)
radiobutton_1.place(relx=0.1, x=110, y=200, anchor=tkinter.CENTER)

radiobutton_2 = customtkinter.CTkRadioButton(master=root, text="test 2", variable=radiobutton_var, value=2,border_width_checked=7)
radiobutton_2.place(relx=0.3, x=110, y=200, anchor=tkinter.CENTER)

radiobutton_3 = customtkinter.CTkRadioButton(master=root, variable=radiobutton_var, value=3,border_width_checked=7)
radiobutton_3.place(relx=0.5, x=110, y=200, anchor=tkinter.CENTER)

radiobutton_4 = customtkinter.CTkRadioButton(master=root, variable=radiobutton_var, value=4,border_width_checked=7)
radiobutton_4.place(relx=0.7, x=110, y=200, anchor=tkinter.CENTER)
radiobutton_var.trace('w', print_var)

root.mainloop()
