#https://www.w3schools.com/python/python_lists_methods.asp
import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        exit(1)
    if len(sys.argv) > 2:
        print("Too many co  mmand-line arguments")
        exit(1)
    if ".csv" not in sys.argv[1]:
        print("Invalid input")
        exit(1)
    
    tab = []
    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for row in reader:
                tab.append(row)
    except FileNotFoundError:
        print("No such file")
        exit(1)
    
    print(tabulate(tab, headers="firstrow", tablefmt="grid"))
    
    
if __name__ == "__main__":
    main()