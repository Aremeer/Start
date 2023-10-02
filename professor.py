import random
import sys

def main():
    level = getLevel()
    totalRightAnswers = 0
    totalWrongAnswers = 0
    while True:
        number1 = generateInteger(level)
        number2 = generateInteger(level)
        answerOriginal = sum([number1, number2])
        answerValue = getAnswer(answerOriginal, number1, number2)
        if totalRightAnswers + totalWrongAnswers == 10:
            print(f"Score: {10 - totalWrongAnswers}")
            sys.exit()
        elif answerValue is True:
            totalRightAnswers = totalRightAnswers + 1
            continue
        elif answerValue is False:
            totalWrongAnswers = totalWrongAnswers + 1
            continue

    
def getLevel():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        if level not in (1, 2, 3):
            continue
        else:
            return level


def generateInteger(level):
    if level == 1: 
        number = random.randrange(1, 9)
        return number
    elif level == 2: 
        number = random.randrange(10, 99)
        return number
    else:
        number = random.randrange(100, 999)
        return number


def getAnswer(answer, number1, number2):
    wrongAnsers = 0
    while True:
        if wrongAnsers == 3:
            print(f"{number1} + {number2} = {answer}")
            wrong = False
            return wrong
        userAnswer = (input(f"{number1} + {number2} = "))
        if userAnswer == answer:
            right = True
            return right
        elif userAnswer != answer:
            print("EEE")
            wrongAnsers = wrongAnsers + 1
            continue
    
    
if __name__ == "__main__":
    main()