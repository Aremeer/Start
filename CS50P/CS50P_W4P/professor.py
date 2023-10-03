import random
import sys

def main():
    level = get_level()
    totalWrongAnswers = 0
    for _ in range(10):
        number1 = generate_integer(level)
        number2 = generate_integer(level)
        answer = sum([number1, number2])
        for _ in range(3):
            try: 
                userInput = int(input(f"{number1} + {number2} = "))
            except ValueError:
                print("EEE")
                continue
            if userInput == answer:
                break
            if userInput != answer:
                print("EEE")
                continue
        else:
            print(f"{number1} + {number2} = {answer}")
            totalWrongAnswers = totalWrongAnswers + 1
            
    print(f"Score: {10 - totalWrongAnswers}")
    sys.exit(0)
        
        
def get_level():
    while True:
            level = input("Level: ")
            try:
                level = int(level)
            except:
                continue
            if level not in (1, 2, 3):
                continue
            return level


def generate_integer(level):
    if level == 1:
        number = random.randrange(0, 9)
        return number
    elif level == 2:
        number = random.randrange(10, 99)
        return number
    else:
        number = random.randrange(100, 999)
        return number


if __name__ == "__main__":
    main()