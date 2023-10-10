#https://www.w3schools.com/python/python_lists_methods.asp
import sys
import csv


def main():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        exit(1)
    if len(sys.argv) > 3:
        print("Too many command-line arguments")
        exit(1)
    
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        print("Invalid input")
        exit(1)
    
    new_csv = []
    with open(sys.argv[1]) as file:
        for line in file:
            line = line.split(",")
            new_line = []
            for word in line:
                word = word.strip('"').strip(" ").strip("\n")
                new_line.append(word)
            pop = new_line.pop(1)
            new_line.insert(0, pop)
            new_csv.append(new_line)
        new_csv.pop(0)
        new_csv.insert(0, ["first","last","house"])
    
    with open(sys.argv[2], "w", newline="") as new_file:
        writer = csv.writer(new_file)
        for _ in new_csv:
            writer.writerow(_)
    
    
if __name__ == "__main__":
    main()