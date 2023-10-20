import csv
import requests
import json



sudoku = requests.get("https://sudoku-api.vercel.app/api/dosuku?query={newboard(limit:5){grids{value,solution,difficulty},results,message}}")
dosuku = sudoku.json()
sudoku = sudoku.json()
sudoku: list = sudoku["newboard"]["grids"][0]["value"]
with open("test3_sudoku.csv", "w", newline="") as file:
    writer = csv.writer(file)
    for row in sudoku:
        writer.writerow(row)

dosuku: list = dosuku["newboard"]["grids"][1]["solution"]
with open("test3_solution.csv", "w", newline="") as file:
    writer = csv.writer(file)
    for row in dosuku:
        writer.writerow(row)