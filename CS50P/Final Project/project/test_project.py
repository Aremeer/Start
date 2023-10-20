import csv
import requests
import json

def read1():
    sudoku = []
    with open("test1_sudoku.csv", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            new = []
            for dig in row:
                dig = int(dig)
                new.append(dig)
            sudoku.append(new)
    return sudoku

def read1_answer():
    answer = []
    with open("test1_solution.csv", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            new = []
            for dig in row:
                dig = int(dig)
                new.append(dig)
            answer.append(new)
    return answer

def read2():
    sudoku2 = []
    with open("test2_sudoku.csv", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            new = []
            for dig in row:
                dig = int(dig)
                new.append(dig)
            sudoku.append(new)
    return sudoku2

def read2_answer():
    answer = []
    with open("test2_solution.csv", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            new = []
            for dig in row:
                dig = int(dig)
                new.append(dig)
            answer.append(new)
    return answer

def read3():
    sudoku3 = []
    with open("test3_sudoku.csv", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            new = []
            for dig in row:
                dig = int(dig)
                new.append(dig)
            sudoku3.append(new)
    return sudoku3

def read3_answer():
    answer = []
    with open("test3_solution.csv", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            new = []
            for dig in row:
                dig = int(dig)
                new.append(dig)
            answer.append(new)
    return answer











