with open("names.csv") as file:
    for line in sorted(file):
        row = line.rstrip().split(",")
        print(f"{value[0]} is a student at {value[1]}")