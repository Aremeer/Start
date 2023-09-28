#https://www.programiz.com/python-programming/methods/built-in/zip
#https://stackoverflow.com/questions/50725199/how-to-make-an-if-inside-a-for-loop-run-only-once?answertab=modifieddesc#tab-top
#https://www.geeksforgeeks.org/string-punctuation-in-python/
#https://stackoverflow.com/questions/70319132/how-do-i-get-an-item-from-a-list-by-just-knowing-its-position-in-a-list
#https://datagy.io/python-list-alphabet/
#https://stackoverflow.com/questions/67180679/compare-previous-and-next-values-when-looping-through-a-list-in-python
#i used all the sources and my code is still awful

import string
punctuation = list(string.punctuation)

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if start_2_letters(s) is True and max_6_char(s) is True:
        if numb_in_end(s) is True and max_6_char(s) is True:       
            return True
    else:
        return False

def start_2_letters(s):
    if s[0:1].isalpha():
          return True

def max_6_char(s):
     if 2 <= len(s) <= 6:
        return True

def numb_in_end(s):
    ran = True
    for x, n in enumerate(s[2:6], start=2):
        nn = str(n)
        if x == len(s)-1:
            return True
        if nn.isdigit():
            if nn == "0" and ran == True:
                ran = False
                return False
            for i in str(s[x+1]):
                if i.isalpha():
                    return False

def no_punct(s):
    for i in s:
        if i in punctuation:
            return False
    else:
        return True

main()