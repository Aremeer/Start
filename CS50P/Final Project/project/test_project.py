import csv
import requests
import json

test1 = "test1_sudoku.csv"
test11 = "test1_solution.csv"
test2 = "test2_sudoku.csv"
test22 = "test2_solution.csv"
test3 = "test3_sudoku.csv"
test33 = "test3_solution.csv"



def read1(s):
    sudoku = []
    with open(s, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            new = []
            for dig in row:
                dig = int(dig)
                new.append(dig)
            sudoku.append(new)
    return sudoku

def read1_answer(s):
    answer = []
    with open(s, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            new = []
            for dig in row:
                dig = int(dig)
                new.append(dig)
            answer.append(new)
    return answer











