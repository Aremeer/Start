from datetime import date
import re


class DateOfBirth:
    def __init__(self, date_of_birth):
        self.date = date_of_birth
        if matches := re.match(r"^(\d{4})-(\d{2})-(\d{2})$", date_of_birth):
            year, month, day = matches.group(1,2,3)
            if year > str(date.today())[0:3]: exit("Invalid year")
            if int(month) > 12: exit("Invalid month")
            if int(day) > 31: exit("invalid day")
            self.year = year
            self.month = month
            self.day = day
        else: exit("Invalid input")

    def __str__(self):
        return f"{self.year}-{self.month}-{self.day}"

    @classmethod
    def get(cls):
        date = input("Date of birth: ")
        return cls(date)



def main():
    print(DateOfBirth.get())











if __name__ == "__main__":
    main()