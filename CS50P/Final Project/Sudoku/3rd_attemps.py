


import csv
import random



#calculate strting-potential
#set current-potentioal = starting-potential
#try first CP and expand
#move next, recalc CP and use one
#repeat until no CP left if so backtrack and try again






def main():
    sudoku_x = read()
    box_i = 0
    boxes = []
    index = 0
    for y in range(9):
        count = 0
        for x in range(9):
            if count == 2:
                count = 0
                box_i += 1
            box = {
                "index":index,
                "value":sudoku_x[y][x],
                "row":y,
                "column":x,
                "box":box_i,
                "starting_potential":[],
                "cuurent_pontetial":[]
                }
            index += 1
            boxes.append(box)

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











