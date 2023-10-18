#https://www.w3schools.com/python/python_json.asp
#https://www.w3schools.com/python/ref_requests_response.asp

import csv
import json
import requests




def main():
    sudoku = requests.get("https://sudoku-api.vercel.app/api/dosuku?query={newboard(limit:1){grids{value}}}")
    sudoku = sudoku.json()
    sudoku: list = sudoku["newboard"]["grids"][0]["value"]
    with open("api.csv", "w", newline="") as file:
        writer = csv.writer(file)
        for row in sudoku:
            writer.writerow(row)






if __name__ in "__main__":
    main()