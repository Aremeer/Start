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

def main():
    date_of_birth = input("Date of birth: ")
    print(code(date_of_birth))

def code(date_of_birth):
    try: date_of_birth = date.fromisoformat(date_of_birth)
    except ValueError: exit("Invalid Input")
    if date_of_birth.year > date.today().year: exit("Wrong date")
    days = date.today() - date_of_birth
    words = p.number_to_words(days.days*24*60, andword="")
    return(f"{words.capitalize()} minutes")

if __name__ == "__main__":
    main()