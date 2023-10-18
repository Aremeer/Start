#i need 3x3 frames
#and 3x3 frames inside frames




#https://sudoku-api.vercel.app/
#https://www.youtube.com/watch?v=HUdPRoGlNwc
#https://customtkinter.tomschimansky.com/documentation/widgets/entry/

import customtkinter as ctk
from sudoku import get_sudoku_csv
import csv
import random

class MySmallFrame(ctk.CTkFrame):
    def __init__(self, master, numbers):
        super().__init__(master)
        for c in range(9):
            number_list = numbers[c]
            for r in range(9):
                number = number_list[r]
                self.textbox = ctk.CTkTextbox(master=self, height=54, width=54)
                self.textbox.grid(row=r, column=c, padx=2, pady=2, sticky="nswe")
                self.textbox.insert("0.0", number)
        
        


class MyFramesFrame(ctk.CTkFrame):
    def __init__(self, master, numbers):
        super().__init__(master)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(3, weight=1)
        
        self.small_frame = MySmallFrame(self, numbers)
        self.small_frame.configure(border_width=4, border_color="#FFFFFF")
        self.small_frame.grid(row=0, column=0, padx=0, pady=0, sticky="nwse")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        numbers = []
        with open("sudoku.csv", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                numbers.append(row)
        self.title("Sudoku")
        self.geometry("600x700")
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        
        self.button = ctk.CTkButton(self, text="New Game")
        self.button.grid(row=1, column=0, padx=10, pady=10, sticky="nw", columnspan=1)
        
        self.button = ctk.CTkButton(self, text="Solve")
        self.button.grid(row=1, column=0, padx=10, pady=10, sticky="ne", columnspan=1)

        self.frame = MyFramesFrame(self, numbers)
        self.frame.configure()
        self.frame.grid(row=0, column=0, padx=10, pady=10, sticky="nwse")


app = App()
app.mainloop()