
import csv
import json
import requests




def main():
    sudoku_x, sudoku_y = read()
    box = []
    
    
    
    
    
    
    
    
    for y in range(9):
        for x in range(9):
            boolean, box = check(sudoku_x, sudoku_y, y, x, box)
            print(boolean)

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
    sudoku_y = []
    with open("api.csv", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            new = []
            for dig in row:
                dig = int(dig)
                new.append(dig)
            sudoku_x.append(new)
        for x in range(9):
            row = []
            for y in range(9):
                row.append(sudoku_x[y][x])
            sudoku_y.append(row)
        return sudoku_x, sudoku_y

def check(sudoku_x, sudoku_y, y, x, box):
    reference = [1,2,3,4,5,6,7,8,9]
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
        return True, box
    else: return False, box



if __name__ in "__main__":
    main()