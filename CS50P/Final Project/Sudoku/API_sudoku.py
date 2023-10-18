import csv
import json
import requests




def main():
    sudoku = requests.get("https://sudoku-api.vercel.app/api/dosuku?query={newboard(limit:1){grids{value}}}")
    print(json.dumps)
    (sudoku.json())
    print(sudoku)







if __name__ in "__main__":
    main()