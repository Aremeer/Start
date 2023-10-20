


import csv
import random
import os 
import time



#set current-potentioal--------
#try first CP and expand-----
#move next, recalc CP and use one-----
#repeat until no CP left if so backtrack and try again





def main():
    sudoku_x = read()
    sudokus = get(sudoku_x)
    current_index = 0
    while True:
        if sudokus[current_index]["solid"] == True:
            current_index+= 1
            print(current_index)
            if current_index == 80 or current_index < 0:
                break
        if sudokus[current_index]["solid"] == False:
            difference = check(sudokus, current_index)
            if len(difference) == 1:
                sudokus[current_index]["value"] = int(difference[0])
                os.system("cls")
                print(current_index,"diff", difference)
                printer(sudokus)
                current_index +=1
                
                continue
            elif len(difference) > 1:
                sudokus[current_index]["value"] = difference.pop(0)
                sudokus[current_index]["potential"] = difference
                os.system("cls")
                print(current_index,"diff",  difference)
                printer(sudokus)
                current_index +=1
                
                continue
            else:
                time.sleep(1)
                while True:
                    if sudokus[current_index]["solid"] == True:
                        current_index -= 1
                        os.system("cls")
                        print(current_index, "is a solid")
                        printer(sudokus)
                    elif current_index < 0:
                        break
                    else:
                        try:
                            sudokus[current_index]["potential"]
                        except KeyError:
                            sudokus[current_index]["value"] = 0
                            current_index -= 1
                            os.system("cls")
                            print(current_index, "has no potential")
                            printer(sudokus)
                            
                            continue
                        if len(sudokus[current_index]["potential"]) == 1:
                            sudokus[current_index]["value"]  = sudokus[current_index]["potential"][0]
                            sudokus[current_index]["potential"].pop(0)
                            os.system("cls")
                            print(current_index,"potential",  sudokus[current_index]["potential"])
                            printer(sudokus)
                            current_index +=1
                            
                            break
                        if len(sudokus[current_index]["potential"]) > 1:
                            sudokus[current_index]["value"] = sudokus[current_index]["potential"][0]
                            sudokus[current_index]["potential"].pop(0)
                            os.system("cls")
                            print(current_index,"potential", sudokus[current_index]["potential"])
                            printer(sudokus)
                            current_index +=1
                            
                            break
    os.system("cls")
    printer(sudokus)

def check(sudokus, current_index):
        box = []
        box_value = sudokus[current_index]["box"]
        for dict in sudokus:
            key = dict["box"]
            if key == box_value:
                box.append(int(dict["value"]))
        
        row=[]
        row_value = sudokus[current_index]["row"]
        for dict in sudokus:
            key = dict["row"]
            if key == row_value:
                row.append(int(dict["value"]))
        
        column = []
        column_value = sudokus[current_index]["column"]
        for dict in sudokus:
            key = dict["column"]
            if key == column_value:
                column.append(int(dict["value"]))
        
        box.sort()
        row.sort()
        column.sort()
        reference = [0,1,2,3,4,5,6,7,8,9]
        diff = list(set(reference)-set(box))
        diff = list(set(diff)-set(row))
        diff = list(set(diff)-set(column))
        return diff

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
                "pontetial":[],
                "solid":True
                }
            if count == 2:
                count = 0
                box_i += 1
            else:
                count += 1
            index += 1
            if box["value"] == 0:
                box["solid"] = False
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

def printer(s):
    print(
    f"""
    {s[0]["value"]}{s[1]["value"]}{s[2]["value"]}|{s[3]["value"]}{s[4]["value"]}{s[5]["value"]}|{s[6]["value"]}{s[7]["value"]}{s[8]["value"]}
    {s[9]["value"]}{s[10]["value"]}{s[11]["value"]}|{s[12]["value"]}{s[13]["value"]}{s[14]["value"]}|{s[15]["value"]}{s[16]["value"]}{s[17]["value"]}
    {s[18]["value"]}{s[19]["value"]}{s[20]["value"]}|{s[21]["value"]}{s[22]["value"]}{s[23]["value"]}|{s[24]["value"]}{s[25]["value"]}{s[26]["value"]}
    -----------
    {s[27]["value"]}{s[28]["value"]}{s[29]["value"]}|{s[30]["value"]}{s[31]["value"]}{s[32]["value"]}|{s[33]["value"]}{s[34]["value"]}{s[35]["value"]}
    {s[36]["value"]}{s[37]["value"]}{s[38]["value"]}|{s[39]["value"]}{s[40]["value"]}{s[41]["value"]}|{s[42]["value"]}{s[43]["value"]}{s[44]["value"]}
    {s[45]["value"]}{s[46]["value"]}{s[47]["value"]}|{s[48]["value"]}{s[49]["value"]}{s[50]["value"]}|{s[51]["value"]}{s[52]["value"]}{s[53]["value"]}
    -----------
    {s[54]["value"]}{s[55]["value"]}{s[56]["value"]}|{s[57]["value"]}{s[58]["value"]}{s[59]["value"]}|{s[60]["value"]}{s[61]["value"]}{s[62]["value"]}
    {s[63]["value"]}{s[64]["value"]}{s[65]["value"]}|{s[66]["value"]}{s[67]["value"]}{s[68]["value"]}|{s[69]["value"]}{s[70]["value"]}{s[71]["value"]}
    {s[72]["value"]}{s[73]["value"]}{s[74]["value"]}|{s[75]["value"]}{s[76]["value"]}{s[77]["value"]}|{s[78]["value"]}{s[79]["value"]}{s[80]["value"]}
    """
    )
















if __name__ == "__main__":
    main()










