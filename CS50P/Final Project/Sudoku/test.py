x = [3, 1, 2]
y = [1, 2, 3]
x.sort()
if x == y:
    print("True")
else: print("False")
print(x)


if y in [0,1,2] and x in [3,4,5]:
        box = []
        lis = sudoku_x[0]
        box.extend(lis[3:6])
        lis = sudoku_x[1]
        box.extend(lis[3:6])
        lis = sudoku_x[1]
        box.extend(lis[3:6])
    
    if y in [0,1,2] and x in [6,7,8]:
        box = []
        lis = sudoku_x[0]
        box.extend(lis[6:9])
        lis = sudoku_x[1]
        box.extend(lis[6:9])
        lis = sudoku_x[1]
        box.extend(lis[6:9])
    
    if y in [3,4,5] and x in [0,1,2]:
        box = []
        lis = sudoku_x[0]
        box.extend(lis[0:3])
        lis = sudoku_x[1]
        box.extend(lis[0:3])
        lis = sudoku_x[1]
        box.extend(lis[0:3])
    
    if y in [3,4,5] and x in [3,4,5]:
        box = []
        lis = sudoku_x[3]
        box.extend(lis[3:6])
        lis = sudoku_x[4]
        box.extend(lis[3:6])
        lis = sudoku_x[5]
        box.extend(lis[3:6])
    
    if y in [3,4,5] and x in [6,7,8]:
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