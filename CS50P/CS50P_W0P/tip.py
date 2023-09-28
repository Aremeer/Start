def main():
    dollars = dollars_to_float(input("How much was the meal? ").strip("$").lower())
    percent = percent_to_float(input("What percentage would you like to tip? ").strip("%").lower())
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(x):
    i = float(x)
    return i



def percent_to_float(x):
    i = float(x)/100
    return i


main()