
import csv
import json
import requests




def main():
    sudoku_x, sudoku_y = read()
    print(sudoku_x, "\n")
    print(sudoku_y, "\n")
    for y in range(9):
        for x in range(9):
            boolean = check(sudoku_x, sudoku_y, y, x)
            print(boolean)

def get():
    sudoku = requests.get("https://sudoku-api.vercel.app/api/dosuku?query={newboard(limit:1){grids{solution}}}")
    sudoku = sudoku.json()
    sudoku: list = sudoku["newboard"]["grids"][0]["solution"]
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

def check(sudoku_x, sudoku_y, y, x):
    reference = [1,2,3,4,5,6,7,8,9]
    if y in [0,1,2] and x in [0,1,2]:
        box = []
        lis = sudoku_x[0]
        box.extend(lis[0:3])
        lis = sudoku_x[1]
        box.extend(lis[0:3])
        lis = sudoku_x[1]
        box.extend(lis[0:3])
    
    

    box.sort()
    result_y = sudoku_y[y]
    result_y.sort()
    result_x = sudoku_x[x]
    result_x.sort()
    print(sudoku_x, "\n")
    print(sudoku_y, "\n")
    print(box, "\n")
    print(result_y, "\n")
    print(result_x, "\n")
    if box == reference and result_y == reference and result_x == reference:
        return True
    else: return False



if __name__ in "__main__":
    main()