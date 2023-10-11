import random
import sys

def main():
    levelRange = askForNumber()
    level = random.randrange(1, levelRange+1)
    guessNumber(level)


def askForNumber():
    while True:
        try:
            levelRange = int(input("Level: "))
        except ValueError:
            continue
        if levelRange < 1:
            continue
        else:
            return levelRange


def guessNumber(level):
    while True:
        try:
            guess = int(input("Guess: "))
            if guess == level:
                sys.exit(print("Just right!"))
            elif guess < level:
                print("Too small!")
                continue
            else:
                print("Too large!")
                continue
        except ValueError:
            continue



if __name__ == "__main__":
    main()