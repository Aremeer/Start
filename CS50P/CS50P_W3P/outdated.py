#https://stackabuse.com/how-to-split-string-on-multiple-delimiters-in-python/
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

import re

def main():
    date = getWrongDate()
    print(date)
    
def getWrongDate():
    while True:
        date = input("Date: ").lower().title()
        numberPattern = r'^\d{1,2}/\d{1,2}/\d{4}$'
        txtPattern = r"[a-zA-Z]+\s\d{1,2},\s\d{4}"
        if re.match(numberPattern, date):
            return date
        if re.match(txtPattern, date):
            return date
        else:
            break
        
#def fixWrongDate(wrongDate):

main()