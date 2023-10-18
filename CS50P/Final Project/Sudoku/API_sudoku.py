#https://www.w3schools.com/python/python_json.asp
#https://www.w3schools.com/python/ref_requests_response.asp

import csv
import json
import requests




def main():
    sudokux, sudokuy = read()
    posx = 0
    posy = 0
    boolean = check(sudokux, sudokuy, posx, posy)
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
    sudokux = []
    sudokuy = []
    with open("api.csv", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            new = []
            for dig in row:
                dig = int(dig)
                new.append(dig)
            sudokux.append(new)
        print(sudokux)
        for x in range(9):
            row = []
            for y in range(9):
                row.append(sudokux[y][x])
            sudokuy.append(row)
        print(f"{sudokux}\n,\n{sudokuy}")
        return sudokux, sudokuy

def check(sudokux, sudokuy, x, y):
    ref = [1,2,3,4,5,6,7,8,9]
    
    if x in ref and y in ref and




if __name__ in "__main__":
    main()