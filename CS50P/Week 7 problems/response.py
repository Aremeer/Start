#https://pypi.org/project/validator-collection/#description
from validator_collection import checkers

def main():
        print(check(input("What's your email adres? ")))

def check(s):
    try:
        if checkers.is_email(s):
            return "Valid"
        else:
            return "Invalid"
    except:
        return "Invalid"

if __name__ == "__main__":
    main()