import re
import sys

def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match := re.search(r"^([1-9]|1[0-2])(?:\:([0-5][0-9]))?\s(AM|PM)\sto\s([1-9]|1[0-2])(?:\:([0-5][0-9]))?\s(AM|PM)$", s):
        first_hour, first_minute, second_hour, second_minute = match.group(1,2,4,5)
        first_ampm, second_ampm = match.group(3,6)
        
        if first_ampm == "AM":
            if first_hour == "12":
                first_hour = "00"
        if first_ampm == "PM":
            if first_hour == "12":
                pass
            else:
                first_hour = str(int(first_hour) ++ 12)
        
        if second_ampm == "AM":
            second_hour = "00"
        if second_ampm== "PM":
            if second_hour == "12":
                pass
            else:
                second_hour = str(int(second_hour) ++ 12)
        
        
        if first_minute == None: first_minute = "00"
        if second_minute == None: second_minute = "00"
        return f"{first_hour}:{first_minute} to {second_hour}:{second_minute}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()