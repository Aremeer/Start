import sys
#got some help in discord

def main():


    names = inputName()
    if len(names) == 1:
        print(f"Adieu, adieu, to {names[0]}")
    elif len(names) == 2:
        print(f"Adieu, adieu, to {names[0]} and {names[1]}")
    else:
        print(f"Adieu, adieu, to {', '.join(names[:-1])}, and {names[-1]}")


def inputName():
    multipleNames = []
    while True:
        try:
            name = (input("Name: "))
            multipleNames.append(name)
        except EOFError:
            if len(multipleNames) < 1:
                print("Invalid input")
                sys.exit(0)
            else:
                return multipleNames


if __name__ == "__main__":
    main()