import string
punctuation = string.punctuation

def main():
    plate = input("Plate: ")
    if is_valid(plate): print("Valid")
    else: print("Invalid")

def is_valid(plate):
    if start_2_letters(plate) and max_6_char(plate) and no_punct(plate) and numb_in_end(plate):
        return True
    else: return False

def start_2_letters(plate):
    if plate[0:1].isalpha(): return True
    else: return False

def max_6_char(plate):
     if 2 <= len(plate) <= 6: return True
     else: return False

def no_punct(plate):
    for text in plate:
        if text in punctuation:
            return False
    else: return True
    
def numb_in_end(plate):
    ran = False
    for plateIndex, plateCharacter in enumerate(plate):
        strPlateCharacter = str(plateCharacter)
        if strPlateCharacter.isdigit():
            if strPlateCharacter == "0" and ran == False:
                return False
            ran = True
        if strPlateCharacter.isdigit() and plateIndex == len(plate)-2:
            for strPlateCharacter in plate[plateIndex+1]:
                if strPlateCharacter.isalpha(): return False
    else: return True
         
main()