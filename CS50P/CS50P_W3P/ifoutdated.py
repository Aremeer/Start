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
import string
punctuations = string.punctuation
        

def main():
    wrongDate = getWrongDate()
    date = fixWrongDate(wrongDate)
    print(date)
    
def getWrongDate():
    while True:
        date = input("Date: ").lower().title()
        table = date.maketrans(",./", "   ")
        date = date.translate(table)
        date = date.split()
        if len(date) == 3: pass
        if len(date[1]) > 2 or date[1].isalpha(): continue
        if len(date[2]) > 4 or date[2].isalpha(): continue
        if len(date[0]) <= 2 or date[0] in months: pass
        else: continue
        return date

def fixWrongDate(wrongDate):
    day = int(wrongDate[1])
    try:
        x = int(wrongDate[1])
        month = int(months.index(wrongDate[0]))+1
        date = f"{wrongDate[2]}-{month:02}-{day:02}"
        return date
    except ValueError:
        month = wrongDate[0]
        date = f"{wrongDate[2]}-{month:02}-{day:02}"
    return date
main()