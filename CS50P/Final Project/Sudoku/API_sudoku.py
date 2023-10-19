
import csv
import json
import requests




def main():
    sudoku_x= read()
    sudoku_y = set_y(sudoku_x)
    progress_x = sudoku_x
    progress_y = sudoku_y
    
    box = []
    boolean, box = check(progress_y, progress_y, box)
    
    box = []
    look_for_number(progress_y, progress_y, box)
    
    print(boolean)
    

def look_for_number(sudoku_x, sudoku_y, box):
    #if dig = 0: check if potential len(dig) == 1 write down, start over
    #hope that it works
    for y in range(9):
        row = sudoku_x[y]
        for x, val in enumerate(row):
            passes = [y, x]
            if val != 0:
                if y in [0,1,2] and x in [0,1,2]:
                    box = []
                    lis = sudoku_x[0]
                    box.extend(lis[0:3])
                    lis = sudoku_x[1]
                    box.extend(lis[0:3])
                    lis = sudoku_x[2]
                    box.extend(lis[0:3])
                
                if y in [0,1,2] and x in [3,4,5]:
                    box = []
                    lis = sudoku_x[3]
                    box.extend(lis[3:6])
                    lis = sudoku_x[4]
                    box.extend(lis[3:6])
                    lis = sudoku_x[5]
                    box.extend(lis[3:6])
                
                if y in [0,1,2] and x in [6,7,8]:
                    box = []
                    lis = sudoku_x[6]
                    box.extend(lis[6:9])
                    lis = sudoku_x[7]
                    box.extend(lis[6:9])
                    lis = sudoku_x[8]
                    box.extend(lis[6:9])
                
                if y in [3,4,5] and x in [0,1,2]:
                    box = []
                    lis = sudoku_x[0]
                    box.extend(lis[0:3])
                    lis = sudoku_x[1]
                    box.extend(lis[0:3])
                    lis = sudoku_x[2]
                    box.extend(lis[0:3])
                
                if y in [3,4,5] and x in [3,4,5]:
                    box = []
                    lis = sudoku_x[3]
                    box.extend(lis[3:6])
                    lis = sudoku_x[4]
                    box.extend(lis[3:6])
                    lis = sudoku_x[5]
                    box.extend(lis[3:6])
                
                if y in [3,4,53] and x in [6,7,8]:
                    box = []
                    lis = sudoku_x[6]
                    box.extend(lis[6:9])
                    lis = sudoku_x[7]
                    box.extend(lis[6:9])
                    lis = sudoku_x[8]
                    box.extend(lis[6:9])
                
                if y in [6,7,8] and x in [0,1,2]:
                    box = []
                    lis = sudoku_x[0]
                    box.extend(lis[6:9])
                    lis = sudoku_x[1]
                    box.extend(lis[6:9])
                    lis = sudoku_x[2]
                    box.extend(lis[6:9])
                
                if y in [6,7,8] and x in [3,4,5]:
                    box = []
                    lis = sudoku_x[3]
                    box.extend(lis[6:9])
                    lis = sudoku_x[4]
                    box.extend(lis[6:9])
                    lis = sudoku_x[5]
                    box.extend(lis[6:9])
                
                if y in [6,7,8] and x in [6,7,8]:
                    box = []
                    lis = sudoku_x[6]
                    box.extend(lis[6:9])
                    lis = sudoku_x[7]
                    box.extend(lis[6:9])
                    lis = sudoku_x[8]
                    box.extend(lis[6:9])
                
                
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
                
                difference = [set(reference)-set(sorted_box_l)]
                difference = [set(difference)-set(result_y_l)]
                difference = [set(difference)-set(result_y_l)]
                
                if len(difference) > 1:
                    pass
                if len(difference) == 1:
                    sudoku_x


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