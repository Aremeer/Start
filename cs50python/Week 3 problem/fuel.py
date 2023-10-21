#got some syntax form https://www.w3schools.com/python
""""""
def main():
    percentFuel = getPercentFuel("Fraction: ")
    if 99 > percentFuel > 1:
        print(f"{int(percentFuel)}%")
    if percentFuel <= 1:
        print("E")
    if percentFuel >= 99:
        print("F")

def getPercentFuel(prompt):
    while True:
        numbersList = input(prompt).split("/")
        if 2 > len(numbersList) > 2:
            continue
        try:
            x = int(numbersList[0])
            y = int(numbersList[1])
        except (ValueError):
            continue
        if x < 0 or y <= 0 or x > y:
            continue
        z = round(float(x/y)*100)
        return z

main()