def main():
    fraction = input("Fraction")
    fuel = convert(fraction)
    print(f"{fuel}")

def convert(fraction):
    fraction = fraction.split("/")
    if fraction[0].isalpha() or fraction[1].isalpha():
        raise ValueError
    
    x = int(fraction[0])
    y = int(fraction[1])
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError
    percentage = round(x/y*100)
    return percentage


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%" 

if __name__ == "__main__":
    main()