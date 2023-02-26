#use google auth for password
import customtkinter
import tkinter
import encode

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

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
button = customtkinter.CTkButton(master=frame, text="notLogin", command=encode.ownAlgoEncoder,width=120,height=32,border_width=1,corner_radius=8)
button.pack(pady=12, padx = 12)
button.place(relx=0.1, rely=0.95, anchor=tkinter.CENTER)

#progress bar
progressbar = customtkinter.CTkProgressBar(master=frame,width=160,height=20,border_width=5)
progressbar.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
progressbar.set(0.1)

root.mainloop()
