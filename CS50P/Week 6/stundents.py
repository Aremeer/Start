import csv

students = []
with open("names.csv") as file:
    reader = csv.DictReader(file)
    for name, home in reader:
        students.append({"name": name, "home": home})

        
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")




