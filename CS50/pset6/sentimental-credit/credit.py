import re


def main():
    card = input("Number: ")
    valid = is_valid(card)
    if valid and is_master(card):
        print("MASTERCARD")
    elif valid and is_amex(card):
        print("AMEX")
    elif valid and is_visa(card):
        print("VISA")
    else:
        print("INVALID")


def is_master(card):
    i = int(card[1])
    if (len(card) == 16 and card[0] == "5" and (i >= 1 or i <= 5)):
        return True
    else:
        return False

def is_amex(card):
    i = int(card[1])
    if (len(card) == 15 and card[0] == "3" and (i == 4 or i == 7)):
        return True
    else:
        return False

def is_visa(card):
    l = len(card)
    if ((l == 13 or l == 16) and card[0] == "4"):
        return True
    else:
        return False

def is_valid(card):
    card = card[::-1]
    first = 0
    second = 0
    for i in range(1, int(len(card)), 2):
        number = int(card[i]) * 2
        if number > 9:
            number = number - 9
        first += number
    for i in range(0, int(len(card)), 2):
        second += int(card[i])
    result = first + second
    if result % 10 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    main()