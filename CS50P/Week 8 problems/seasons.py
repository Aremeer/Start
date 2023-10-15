import datetime
from datetime import date
import re

class DateOfBirth:
    def __init__(self, date_of_birth):
        self.today = date.today()
        try:
            date_of_birth = date.fromisoformat(date_of_birth)
            date_of_birth = date_of_birth.max(date_of_birth.year, date_of_birth.month, date_of_birth.day)
        except ValueError: exit("Invalid Input")
        
    def __str__(self):
        return(str(self.today))
    
    
    @classmethod
    def get(cls):
        date_of_birth = input("Date of birth: ")
        return cls(date_of_birth)



def main():
    date = (DateOfBirth.get())
    print(date)




if __name__ == "__main__":
    main()