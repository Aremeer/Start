#i need 3x3 frames
#and 3x3 frames inside frames




#https://sudoku-api.vercel.app/
#https://www.youtube.com/watch?v=HUdPRoGlNwc
#https://customtkinter.tomschimansky.com/documentation/widgets/entry/

import customtkinter as ctk
from sudoku import get_sudoku_csv
import csv
import time



class MyFramesFrame(ctk.CTkFrame):
    def __init__(self, master, numbers):
        super().__init__(master)
        c=0
        r=0
        rr=0
        for n in range(9):
            if numbers[n] == "0":
                number = ""
            else: number = numbers[n]
            self.textbox = ctk.CTkTextbox(master=self, height=54, width=54)
            self.textbox.grid(row=r, column=c, padx=2, pady=2, sticky="nswe")
            self.textbox.insert("0.0", number)
            if c==2:
                c=0 
            else:
                c+=1
            if rr==2: 
                r+=1
                rr=0
            else:
                rr+=1

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        numbers = []
        with open("api.csv", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                numbers.append(row)
        self.title("Sudoku")
        self.geometry("600x700")
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        
        self.button = ctk.CTkButton(self, text="New Game")
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="nw", columnspan=1)
        
        self.button = ctk.CTkButton(self, text="Solve")
        self.button.grid(row=3, column=2, padx=10, pady=10, sticky="ne", columnspan=1)
        
        c=0
        r=0
        rr=0
        for n in range(9):
            self.frame = MyFramesFrame(self, numbers[n])
            self.frame.configure(border_width=4, border_color="#FFFFFF")
            self.frame.grid(row=r, column=c, padx=10, pady=10, sticky="nwse")
            if c==2:
                c=0 
            else:
                c+=1
            if rr==2: 
                r+=1
                rr=0
            else:
                rr+=1

app = App()
app.mainloop()