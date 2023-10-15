from datetime import date
import re

class DateOfBirth:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth
        if matches := re.match(r"^\d{4}-\d{2}-\d{2}$", self.date_of_birth):
            year, month, day = [date.fromisoformat(date_of_birth)]
            self.year = year
            self.month = month
            self.day = day
        else: exit("Invalid input")

        def changeinto():
            

    def __str__(self):
        return f"{self.year}-{self.month}-{self.day}"

    @classmethod
    def get(cls):
        date_of_birth = input("Date of birth: ")
        return cls(date_of_birth)


def main():
    date = (DateOfBirth.get())
    print(date)











if __name__ == "__main__":
    main()