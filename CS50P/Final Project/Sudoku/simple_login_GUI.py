""""GUI that will be a white backgroud a big box in the top with sudoku appearance, and two buttons at the bottom - randomise, and solve"""

import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

def login():
    print("Test")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login System", font=("Ariel", 24))
label.pack(pady=12, padx=10)

enrty1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
enrty1.pack(pady=12, padx=10)

enrty1 = customtkinter.CTkEntry(master=frame, placeholder_text="Password")
enrty1.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember me")
checkbox.pack(pady=12, padx=10)

root.mainloop()



