#https://www.w3schools.com/python/python_lists_methods.asp
import sys
import csv


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
    
    
    
    
if __name__ == "__main__":
    main()