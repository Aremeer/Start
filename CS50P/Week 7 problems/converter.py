import csv
import re

file_list = ["US","UN"]
file2 = open("converter.csv", "w", newline="")
writer = csv.writer(file2)
with open("table.csv") as file:
    for line in file:
        if match := re.search(r"^([1-9]?[0-2]?):00.(?:AM|PM)(?:.*?)([0-2][0-9]):00$", line):
            line = [match.group(1), match.group(2)]
            writer.writerow(line)

file2_list = []