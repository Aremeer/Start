#searched up syntax https://www.programiz.com/python-programming/string

def main():
    time = input("What time is it? ")
    float_time = convert(time)
    if 7 <= float_time <= 8:
        print("breakfast time")
    elif 12 <= float_time <= 13:
        print("lunch time")
    elif 18 <= float_time <= 19:
        print("dinner time")
    else:
        print("", end="/n")

def convert(time):
    i = time.split(":")
    j = float(i[0]) + float(i[1]) / 60
    return(round(j, 2))


if __name__ == "__main__":
    main()