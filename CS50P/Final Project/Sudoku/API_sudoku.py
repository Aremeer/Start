
import csv
import json
import requests
import os
import time



def main():
    get()
    sudoku_x = read()
    sudoku_y = set_y(sudoku_x)
    progress_x = sudoku_x
    progress_y = sudoku_y
    
    box = []
    i = 0
    while i == 0:
        progress_x, progress_y = look_for_number(progress_x, progress_y)
        if 0 not in progress_x[8] or 0 not in progress_x[7] or 0 not in progress_x[6] or 0 not in progress_x[5]:
            i = 1
        else: i = 0

    boolean, box = check(progress_x, progress_y, box)
    print(
    f"""
    {sudoku_x[0][0:3]}{sudoku_x[0][3:6]}{sudoku_x[0][5:8]}
    {sudoku_x[1][0:3]}{sudoku_x[1][3:6]}{sudoku_x[1][5:8]}
    {sudoku_x[2][0:3]}{sudoku_x[2][3:6]}{sudoku_x[2][5:8]}
    ------------------------------------------------------
    {sudoku_x[3][0:3]}{sudoku_x[2][3:6]}{sudoku_x[3][5:8]}
    {sudoku_x[4][0:3]}{sudoku_x[3][3:6]}{sudoku_x[4][5:8]}
    {sudoku_x[5][0:3]}{sudoku_x[4][3:6]}{sudoku_x[5][5:8]}
    -------------------------------------------------------
    {sudoku_x[6][0:3]}{sudoku_x[5][3:6]}{sudoku_x[6][5:8]}
    {sudoku_x[7][0:3]}{sudoku_x[6][3:6]}{sudoku_x[7][5:8]}
    {sudoku_x[8][0:3]}{sudoku_x[7][3:6]}{sudoku_x[8][5:8]}
    """
    )
    print("The result is:", boolean)

def look_for_number(sudoku_x, sudoku_y):
    box = []
    print(
f"""
{sudoku_x[0][0:3]}{sudoku_x[0][3:6]}{sudoku_x[0][5:8]}
{sudoku_x[1][0:3]}{sudoku_x[1][3:6]}{sudoku_x[1][5:8]}
{sudoku_x[2][0:3]}{sudoku_x[2][3:6]}{sudoku_x[2][5:8]}
------------------------------------------------------
{sudoku_x[3][0:3]}{sudoku_x[2][3:6]}{sudoku_x[3][5:8]}
{sudoku_x[4][0:3]}{sudoku_x[3][3:6]}{sudoku_x[4][5:8]}
{sudoku_x[5][0:3]}{sudoku_x[4][3:6]}{sudoku_x[5][5:8]}
-------------------------------------------------------
{sudoku_x[6][0:3]}{sudoku_x[5][3:6]}{sudoku_x[6][5:8]}
{sudoku_x[7][0:3]}{sudoku_x[6][3:6]}{sudoku_x[7][5:8]}
{sudoku_x[8][0:3]}{sudoku_x[7][3:6]}{sudoku_x[8][5:8]}
"""
)
    for y in range(9):
        row = sudoku_x[y]
        for x, val in enumerate(row):
            if val == 0:
                if y in [0,1,2] and x in [0,1,2]:
                    box = []
                    lis = sudoku_x[0]
                    lis = lis[0:3]
                    box.extend(lis)
                    lis = sudoku_x[1]
                    lis = lis[0:3]
                    box.extend(lis)
                    lis = sudoku_x[2]
                    lis = lis[0:3]
                    box.extend(lis)
                
                elif y in [0,1,2] and x in [3,4,5]:
                    box = []
                    lis = sudoku_x[0]
                    lis = lis[3:6]
                    box.extend(lis)
                    lis = sudoku_x[1]
                    lis = lis[3:6]
                    box.extend(lis)
                    lis = sudoku_x[2]
                    lis = lis[3:6]
                    box.extend(lis)
                
                elif y in [0,1,2] and x in [6,7,8]:
                    box = []
                    lis = sudoku_x[0]
                    lis = lis[6:9]
                    box.extend(lis)
                    lis = sudoku_x[1]
                    lis = lis[6:9]
                    box.extend(lis)
                    lis = sudoku_x[2]
                    lis = lis[6:9]
                    box.extend(lis)
                
                elif y in [3,4,5] and x in [0,1,2]:
                    box = []
                    lis = sudoku_x[3]
                    lis = lis[3:6]
                    box.extend(lis)
                    lis = sudoku_x[4]
                    lis = lis[3:6]
                    box.extend(lis)
                    lis = sudoku_x[5]
                    lis = lis[3:6]
                    box.extend(lis)
                
                elif y in [3,4,5] and x in [3,4,5]:
                    box = []
                    lis = sudoku_x[3]
                    lis = lis[3:6]
                    box.extend(lis)
                    lis = sudoku_x[4]
                    lis = lis[3:6]
                    box.extend(lis)
                    lis = sudoku_x[5]
                    lis = lis[3:6]
                    box.extend(lis)
                
                elif y in [3,4,5] and x in [6,7,8]:
                    box = []
                    lis = sudoku_x[3]
                    lis = lis[3:6]
                    box.extend(lis)
                    lis = sudoku_x[4]
                    lis = lis[3:6]
                    box.extend(lis)
                    lis = sudoku_x[5]
                    lis = lis[3:6]
                    box.extend(lis)
                
                elif y in [6,7,8] and x in [0,1,2]:
                    box = []
                    lis = sudoku_x[6]
                    lis = lis[6:9]
                    box.extend(lis)
                    lis = sudoku_x[7]
                    lis = lis[6:9]
                    box.extend(lis)
                    lis = sudoku_x[8]
                    lis = lis[6:9]
                    box.extend(lis)
                
                elif y in [6,7,8] and x in [3,4,5]:
                    box = []
                    lis = sudoku_x[6]
                    lis = lis[0:3]
                    box.extend(lis)
                    lis = sudoku_x[7]
                    lis = lis[0:3]
                    box.extend(lis)
                    lis = sudoku_x[8]
                    lis = lis[0:3]
                    box.extend(lis)
                
                elif y in [6,7,8] and x in [6,7,8]:
                    box = []
                    lis = sudoku_x[6]
                    lis = lis[0:3]
                    box.extend(lis)
                    lis = sudoku_x[7]
                    lis = lis[0:3]
                    box.extend(lis)
                    lis = sudoku_x[8]
                    lis = lis[0:3]
                    box.extend(lis)
                
                
                sorted_box_l = []
                sorted_box_l.extend(box)
                sorted_box_l.sort()
                result_y_l = []
                result_y_l.extend(sudoku_x[x])
                result_y_l.sort()
                result_x_l = []
                result_x_l.extend(sudoku_y[y])
                result_x_l.sort()
                reference = [0,1,2,3,4,5,6,7,8,9]
                
                difference = list(set(reference)-set(sorted_box_l))
                difference = list(set(difference)-set(result_y_l))
                difference = list(set(difference)-set(result_y_l))
                
                if len(difference) == 1:
                    sudoku_x[y][x] = difference[0]
                    sudoku_y[x][8-y] = difference[0]
                    os.system("cls")
                    return sudoku_x, sudoku_y
                elif len(difference) < 0:
                    os.system("cls")
                    return sudoku_x, sudoku_y
                else:
                    pass
    os.system("cls")
    return sudoku_x, sudoku_y

def get():
    sudoku = requests.get("https://sudoku-api.vercel.app/api/dosuku?query={newboard(limit:1){grids{value}}}")
    sudoku = sudoku.json()
    sudoku: list = sudoku["newboard"]["grids"][0]["value"]
    with open("api.csv", "w", newline="") as file:
        writer = csv.writer(file)
        for row in sudoku:
            writer.writerow(row)
    return writer

def read():
    sudoku_x = []
    with open("api.csv", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            new = []
            for dig in row:
                dig = int(dig)
                new.append(dig)
            sudoku_x.append(new)
    return sudoku_x

def set_y(sudoku_x):
    sudoku_y = []
    for x in range(9):
            row = []
            for y in range(9):
                row.append(sudoku_x[y][x])
            sudoku_y.append(row)
    return sudoku_y

def check(sudoku_x, sudoku_y, box):
    reference = [1,2,3,4,5,6,7,8,9]
    for y in range(9):
        for x in range(9):
            if y in [0] and x in [0]:
                box = []
                lis = sudoku_x[0]
                box.extend(lis[0:3])
                lis = sudoku_x[1]
                box.extend(lis[0:3])
                lis = sudoku_x[2]
                box.extend(lis[0:3])
            
            if y in [0] and x in [3]:
                box = []
                lis = sudoku_x[3]
                box.extend(lis[3:6])
                lis = sudoku_x[4]
                box.extend(lis[3:6])
                lis = sudoku_x[5]
                box.extend(lis[3:6])
            
            if y in [0] and x in [6]:
                box = []
                lis = sudoku_x[6]
                box.extend(lis[6:9])
                lis = sudoku_x[7]
                box.extend(lis[6:9])
                lis = sudoku_x[8]
                box.extend(lis[6:9])
            
            if y in [3] and x in [0]:
                box = []
                lis = sudoku_x[0]
                box.extend(lis[0:3])
                lis = sudoku_x[1]
                box.extend(lis[0:3])
                lis = sudoku_x[2]
                box.extend(lis[0:3])
            
            if y in [3] and x in [3]:
                box = []
                lis = sudoku_x[3]
                box.extend(lis[3:6])
                lis = sudoku_x[4]
                box.extend(lis[3:6])
                lis = sudoku_x[5]
                box.extend(lis[3:6])
            
            if y in [3] and x in [6]:
                box = []
                lis = sudoku_x[6]
                box.extend(lis[6:9])
                lis = sudoku_x[7]
                box.extend(lis[6:9])
                lis = sudoku_x[8]
                box.extend(lis[6:9])
            
            if y in [6] and x in [0]:
                box = []
                lis = sudoku_x[0]
                box.extend(lis[6:9])
                lis = sudoku_x[1]
                box.extend(lis[6:9])
                lis = sudoku_x[2]
                box.extend(lis[6:9])
            
            if y in [6] and x in [3]:
                box = []
                lis = sudoku_x[3]
                box.extend(lis[6:9])
                lis = sudoku_x[4]
                box.extend(lis[6:9])
                lis = sudoku_x[5]
                box.extend(lis[6:9])
            
            if y in [6] and x in [6]:
                box = []
                lis = sudoku_x[6]
                box.extend(lis[6:9])
                lis = sudoku_x[7]
                box.extend(lis[6:9])
                lis = sudoku_x[8]
                box.extend(lis[6:9])
            
            
            sorted_box = []
            sorted_box.extend(box)
            sorted_box.sort()
            result_y = []
            result_y.extend(sudoku_x[x])
            result_y.sort()
            result_x = []
            result_x.extend(sudoku_y[y])
            result_x.sort()
            if sorted_box == reference and result_y == reference and result_x == reference:
                pass
            else: return False, box
    return True, box

if __name__ in "__main__":
    main()