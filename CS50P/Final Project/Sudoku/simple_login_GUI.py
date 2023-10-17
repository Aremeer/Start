""""GUI that will be a white backgroud a big box in the top with sudoku appearance, and two buttons at the bottom - randomise, and solve"""

import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        # add widgets onto the frame, for example:
        self.frame = customtkinter.CTkFrame(master=master, width=180, height=180, border_width=2)
        self.frame.grid(row=0, column=0, padx=2, pady=2)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.grid_rowconfigure(2, weight=1)  # configure grid system
        self.grid_columnconfigure(2, weight=1)
        
        self.my_frame = MyFrame(master=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.my_frame1 = MyFrame(master=self)
        self.my_frame1.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")



app = App()
app.mainloop()



