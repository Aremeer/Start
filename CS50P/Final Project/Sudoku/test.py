import customtkinter as ctk

app = ctk.CTk()
app.title("my app")
app.geometry("400x150")

frame = ctk.CTkFrame(master=app, border_width=2, border_color="#FFFFFF")
frame.grid(row=0, column=0, padx=5, pady=5, sticky="nwse")

lable = ctk.CTkLabel(master=frame)
lable.grid(row=0, column=0, padx=5, pady=5, sticky="nwse")

app.mainloop()