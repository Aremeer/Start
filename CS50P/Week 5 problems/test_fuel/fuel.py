def main():
    fraction = input("Fraction")
    #percentage = convert(fraction)

def convert(fraction):
    fraction = int(fraction.split("/"))
    x = fraction[0]
    y = fraction[1]
    return x, y


#def gauge(percentage):


if __name__ == "__main__":
    main()
#"""convert expects a str in X/Y format as input, wherein each of X and Y is an integer, and returns that fraction as a percentage rounded to the nearest int between 0 and 100, inclusive. If X and/or Y is not an integer, or if X is greater than Y, then convert should raise a ValueError. If Y is 0, then convert should raise a ZeroDivisionError.
#gauge expects an int and returns a str that is:
#"E" if that int is less than or equal to 1,
#"F" if that int is greater than or equal to 99,
#and "Z%" otherwise, wherein Z is that same int."""