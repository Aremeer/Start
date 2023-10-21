import string

punctuations = string.punctuation 

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(txt):
    strippedLowerText = txt.strip(punctuations).lower()
    return(float(strippedLowerText))



def percent_to_float(txt):
    strippedLowerText = txt.strip(punctuations).lower()
    return(float(strippedLowerText)/100)


main()