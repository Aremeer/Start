#https://docs.python.org/3/library/csv.html
#https://www.w3schools.com/python/default.asp



import csv
import random



"""so the idea is that you would create a csv formated list of lists where you have 9 rows.
    key value parirs of keys[1-9]:list[1-9]"""

def main():
    get_sudoku_csv()
    get_sudoku_value()

def get_sudoku_value():
    sudoku_list = []
    with open("sudoku.csv", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            sudoku_list.append(row)
        print(sudoku_list)
        return sudoku_list
def get_sudoku_csv():
    with open("sudoku.csv", "w", newline="") as file:
        writer= csv.writer(file)
        for _ in range(9):
            numbers = []
            range_of_randoms: list = [1,2,3,4,5,6,7,8,9]
            for n_ in range(9):
                random_number: int = random.choice(range_of_randoms)
                numbers.append(random_number)
                range_of_randoms.remove(random_number)
                
            range_of_randoms: list = [1,2,3,4,5,6,7,8,9]
            choesn_numbers: list = []
            for _ in range(random.randint(3,5)):
                random_number: int = random.choice(range_of_randoms)
                range_of_randoms.remove(random_number)
                choesn_numbers.append(random_number)
                
            for n in range(len(choesn_numbers)):
                i = numbers.index(choesn_numbers[n])
                numbers[i] = ""
            writer.writerow(numbers)




if __name__ == "__main__":
    main()