import csv
import requests
import json



sudoku = requests.get("https://sudoku-api.vercel.app/api/dosuku?query={newboard(limit:5){grids{value,solution,difficulty},results,message}}")
sudoku = sudoku.json()
sudoku: list = sudoku["newboard"]["grids"][0]["value"]
with open("test1_sudoku.csv", "w", newline="") as file:
    writer = csv.writer(file)
    for row in sudoku:
        writer.writerow(row)

with open("test1_solution.csv", "w", newline="") as file:
    writer = csv.writer(file)
    for row in sudoku:
        writer.writerow(row)