#https://bobbyhadz.com/blog/python-input-date
#https://stackoverflow.com/questions/69806492/regex-d4-d2-d2

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
from datetime import date
#prompt user for a date mm/dd/yyyy or month dd, yyyy
#output date in YYYY-MM-DD format
#if usre's input is not valid in either format, prompt again
#assume that month has no more than 31 days.
def main():
    while True:
        try:
            dateComponents = promptForDate()
            if dateComponents is False: continue
            dateChecked = checkIfAplpha(dateComponents)
            validDates = checkValidDates(dateChecked)
            month, day, year = [int(item) for item in validDates]
        except (ValueError, TypeError):
            continue
        print(f"{year}-{month:02}-{day:02}")
        break
    
def promptForDate():
    dateComponents = input("Date: ").lower().title()
    patternDigit = "^\d{2}/\d{2}/\d{4}$"
    resultPD = re.match(patternDigit, dateComponents)
    patternAlpha = "^[a-zA-Z]*?\s\d{2},\s\d{4}$"
    resultPA = re.match(patternAlpha, dateComponents)
    if resultPD is False and resultPA is False: 
        return False
    else:  
        table = dateComponents.maketrans(",/", "  ")
        dateComponents = dateComponents.translate(table)
        dateComponents = dateComponents.split()
        return dateComponents

def checkIfAplpha(d):
    if d[0] in months:
        month = months.index(d[0])+1
        d.remove(d[0])
        d.insert(0, month)
        return d
    else:
        return d
    
def checkValidDates(d):
    if int(d[0]) > 12 or int(d[1]) > 31: return False
    else: return d
    
main()