#i need 3x3 frames
#and 3x3 frames inside frames

#https://customtkinter.tomschimansky.com/documentation/widgets/entry/

import customtkinter as ctk


class MyFramesFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(3, weight=1)
        for n in range(3):
            for i in range(3):
                small_frame = ctk.CTkFrame(master=self, border_width=4, border_color="#FFFFFF")
                small_frame.grid(row=n, column=i, padx=0, pady=0, sticky="nwse")
                
                title = ctk.CTkLabel(master=small_frame, text="1", fg_color="transparent")
                title.grid(row=n, column=i, padx=0, pady=0, sticky="nwse")
                

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Sudoku")
        self.geometry("600x700")
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        
        self.button = ctk.CTkButton(self, text="New Game")
        self.button.grid(row=4, column=0, padx=10, pady=10, sticky="s", columnspan=1)
        
        self.button = ctk.CTkButton(self, text="Solve")
        self.button.grid(row=4, column=2, padx=10, pady=10, sticky="s", columnspan=1)
        
        for n in range(3):
            for i in range(3):
                self.frame1 = MyFramesFrame(self)
                self.frame1.configure()
                self.frame1.grid(row=n, column=i, padx=10, pady=10, sticky="nwse")


app = App()
app.mainloop()