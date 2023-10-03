import random
import sys

def main():
    level = get_level()
    totalRightAnswers = int("0")
    for _ in range(10):
        number1 = generate_integer(level)
        number2 = generate_integer(level)
        answer = sum([number1, number2])
        userInput = input(f"{number1} + {number2} = ")
        totalRightAnswers = checkUserAnswer(userInput, answer, number1, number2, totalRightAnswers)
    if totalRightAnswers == None:
        print ("Score: 0")
    else:
        print("Score:", totalRightAnswers)
    exit(0)
    
def get_level(level):
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


def checkUserAnswer(userInput, answer, number1, number2, totalRightAnswers):
    for _ in range(2):
        try:
            userInput = int(userInput)
        except ValueError:
            print("EEE")
            userInput = input(f"{number1} + {number2} = ")
            continue
        if userInput == answer:
            totalRightAnswers = totalRightAnswers + 1
            return totalRightAnswers
        if userInput != answer:
            print("EEE")
            userInput = input(f"{number1} + {number2} = ")
            continue
    print(f"{number1} + {number2} = {answer}")
    print()


if __name__ == "__main__":
    main()