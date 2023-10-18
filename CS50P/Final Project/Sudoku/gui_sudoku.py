#i need 3x3 frames
#and 3x3 frames inside frames





#https://www.youtube.com/watch?v=HUdPRoGlNwc
#https://customtkinter.tomschimansky.com/documentation/widgets/entry/

import customtkinter as ctk
from sudoku import get_sudoku_csv
import csv
import random

class MySmallFrame(ctk.CTkFrame):
    def __init__(self, master, numbers, n):
        super().__init__(master)
        self.textbox = ctk.CTkTextbox(master=self, height=54, width=54)
        self.textbox.grid(row=0, column=0, padx=2, pady=2, sticky="nswe")
        self.textbox.insert("0.0", numbers[n])
        
        


class MyFramesFrame(ctk.CTkFrame):
    def __init__(self, master, numbers):
        super().__init__(master)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(3, weight=1)
        n=0 
        for i in range(3):
            for x in range(3):
                self.small_frame = MySmallFrame(self, numbers, n)
                self.small_frame.configure(border_width=4, border_color="#FFFFFF")
                self.small_frame.grid(row=i, column=x, padx=0, pady=0, sticky="nwse")
                n+=1


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.sudoku_list = []
        with open("sudoku.csv", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                self.sudoku_list.append(row)
        self.title("Sudoku")
        self.geometry("600x700")
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        
        self.button = ctk.CTkButton(self, text="New Game")
        self.button.grid(row=4, column=0, padx=10, pady=10, sticky="s", columnspan=1)
        
        self.button = ctk.CTkButton(self, text="Solve")
        self.button.grid(row=4, column=2, padx=10, pady=10, sticky="s", columnspan=1)
    
    
        n = 0
        for i in range(3):
            for x in range(3):
                numbers: dict = self.sudoku_list[n]
                self.frame = MyFramesFrame(self, numbers)
                self.frame.configure()
                self.frame.grid(row=i, column=x, padx=10, pady=10, sticky="nwse")
                n+=1


app = App()
app.mainloop()