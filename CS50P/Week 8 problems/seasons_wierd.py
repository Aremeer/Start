#https://www.toptal.com/python/python-class-attributes-an-overly-thorough-guide
#https://stackoverflow.com/questions/12412324/python-class-returning-value
#https://pypi.org/project/inflect/
#https://docs.python.org/3/library/datetime.html#datetime.date
#https://www.w3schools.com/python/python_strings_methods.asp
#https://docs.pytest.org/en/7.4.x/
#https://stackoverflow.com/questions/74931773/pytest-ing-a-function-with-no-arguments
from datetime import date
import inflect
p = inflect.engine()

class DateOfBirth:
    def __init__(self, date_of_birth):
        try: self.date_of_birth = date.fromisoformat(date_of_birth)
        except ValueError: exit("Invalid Input")
        
        if self.date_of_birth.year > date.today().year: exit("Wrong date")
    
    def __call__(self):
        return self.date_of_birth


def main():
    date_of_birth = get()
    db = (DateOfBirth(date_of_birth))
    print(turn_to_words(db.date_of_birth))

def get():
    date_of_birth = input("Date of birth: ")
    return date_of_birth

def turn_to_words(x):
    days = date.today() - x
    words = p.number_to_words(days.days*24*60, andword="")
    return (f"{words.capitalize()} minutes")

def code():
    date_of_birth = input("Date of birth: ")
    try: date_of_birth = date.fromisoformat(date_of_birth)
    except ValueError: exit("Invalid Input")
    if date_of_birth.year > date.today().year: exit("Wrong date")
    days = date.today() - date_of_birth
    words = p.number_to_words(days.days*24*60, andword="")
    print(f"{words.capitalize()} minutes")

if __name__ == "__main__":
    main()