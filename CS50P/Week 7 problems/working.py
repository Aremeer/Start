import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    dict = {'12': '12', '1': '13', '2': '14', '3': '15', '4': '16', '5': '17', '6': '18', '7': '19', '8': '20', '9': '21', '10': '22', '11': '23'}
    if match := re.search(r"^([1-9]|1[0-2])(?:\:([0-5][0-9]))?\s(AM|PM)\sto\s([1-9]|1[0-2])(?:\:([0-5][0-9]))?\s(AM|PM)$", s):
        first_hour, first_minute, second_hour, second_minute = match.group(1,2,4,5)
        first_ampm, second_ampm = match.group(3,6)
        
        if first_ampm == "AM" and first_hour == "12":
            first_hour = "00"
        if second_ampm == "AM" and second_hour == "12":
            second_hour = "00"
        
        if first_ampm == "PM":
            first_hour = dict[f"{first_hour}"]
        if second_ampm == "PM":
            second_hour = dict[f"{second_hour}"]
        
        if first_minute == None: first_minute = "00"
        if second_minute == None: second_minute = "00"
        return f"{int(first_hour):02d}:{first_minute} to {int(second_hour):02d}:{second_minute}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()