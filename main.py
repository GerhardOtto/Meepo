#use google auth for password
import customtkinter
import tkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")


def login():
    print("test")
    

def notLogin():
    print("notLogin")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login System", font=("Arial", 24))
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="notNotLogin", command=notLogin)
button.pack(pady=12, padx = 10)

button = customtkinter.CTkButton(master=frame, text="notLogin", command=notLogin,width=120,height=32,border_width=1,corner_radius=8)
button.pack(pady=12, padx = 12)
button.place(relx=0.2, rely=0.5, anchor=tkinter.CENTER)

root.mainloop()
