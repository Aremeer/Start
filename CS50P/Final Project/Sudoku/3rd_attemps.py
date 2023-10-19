


import csv
import random




#set current-potentioal
#try first CP and expand
#move next, recalc CP and use one
#repeat until no CP left if so backtrack and try again






def main():
    sudoku_x = read()
    sudokus = get(sudoku_x)
    
    while True:
        current_index = 0
        
        box = []
        for r in range(9):
            box_value = sudokus[current_index]["box"]
            boxes = []
            for i, value in enumerate(sudokus):
                key = value["box"]
                if key == box_value:
                    boxes.append(i)
            print(boxes)
            break
        
        
        
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









def get(sudoku_x):
    sudoku_x = read()
    sudokus = []
    index = 0
    count = 0
    box_row = 0
    for y in range(9):
        if box_row == 0 or box_row == 1 or box_row == 2:
            box_i = 0
        if box_row == 3 or box_row == 4 or box_row == 5:
            box_i = 3
        if box_row == 6 or box_row == 7 or box_row == 8:
            box_i = 6
        box_row += 1
        for x in range(9):
            box = {
                "index":index,
                "value":sudoku_x[y][x],
                "row":y,
                "column":x,
                "box":box_i,
                "pontetial":[]
                }
            if count == 2:
                count = 0
                box_i += 1
            else:
                count += 1
            index += 1
            sudokus.append(box)
    return sudokus

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


if __name__ == "__main__":
    main()











