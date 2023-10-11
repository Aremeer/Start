import re
import sys
"""In a file called working.py, implement a function called convert that expects a str in either of the 12-hour formats below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00). Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space before each. Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.

9:00 AM to 5:00 PM
9 AM to 5 PM
Raise a ValueError instead if the input to convert is not in either of those formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that someone’s hours will start ante meridiem and end post meridiem; someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).

Structure working.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit, but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys."""

def main():
    print(convert(input("Hours: ")))

#get str
#check format else return ValueError
#return europe
def convert(s):
    if match := re.search(r"^([1-9]|1[0-2])(?:\:([0-5][0-9]))?\s(?:AM|PM)\sto\s([1-9]|1[0-2])(?:\:([0-5][0-9]))?\s(?:AM|PM)$", s):
        first_hour, first_minute, second_hour, second_minute = match.group(1,2,3,4)
        if first_minute == None: first_minute = "00"
        if second_minute == None: second_minute = "00"
        print(f"{first_hour}:{first_minute} to {second_hour}:{second_minute}")
    else:
        raise ValueError


if __name__ == "__main__":
    main()