#i need 3x3 frames
#and 3x3 frames inside frames





#https://www.youtube.com/watch?v=HUdPRoGlNwc
#https://customtkinter.tomschimansky.com/documentation/widgets/entry/

import customtkinter as ctk
from sudoku import get_sudoku_csv
import csv
import os



app = ctk.CTk()
sudoku_list = []
with open("sudoku.csv", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        sudoku_list.append(row)
app.title("Sudoku")
app.geometry("550x600")
app.grid_columnconfigure(3, weight=1)
app.grid_rowconfigure(4, weight=1)

button = ctk.CTkButton(master=app, text="New Game")
button.grid(row=4, column=0, padx=10, pady=10, sticky="n", columnspan=1)

button = ctk.CTkButton(master=app, text="Solve")
button.grid(row=4, column=2, padx=10, pady=10, sticky="n", columnspan=1)

l = 0
for i in range(3):
    for x in range(3):
        numbers: dict = sudoku_list[l]
        frame = ctk.CTkFrame(master=app)
        frame.configure()
        frame.grid(row=i, column=x, padx=10, pady=10, sticky="nwse")
        
        frame.grid_rowconfigure(3, weight=1)
        frame.grid_columnconfigure(3, weight=1)
        n = 0
        for ii in range(3):
            for xx in range(3):
                small_frame = ctk.CTkFrame(master=frame, border_width=4, border_color="#FFFFFF")
                small_frame.grid(row=ii, column=xx, padx=0, pady=0, sticky="nwse")
                small_lable = ctk.CTkLabel(master=small_frame, text=numbers[f"{n+1}"], height=50, width=50)
                small_lable.grid(row=ii, column=xx, padx=2, pady=2, sticky="nwse")
                n+=1
        l+=1




app.mainloop()