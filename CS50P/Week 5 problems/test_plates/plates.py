import string
punctuation = string.punctuation

def main():
    plate = input("Plate: ")
    if is_valid(plate): 
        print("Valid")
    else: 
        print("Invalid")

def is_valid(s):
    
    if len(s) < 2 or len(s) > 6 :
        return False
    else:
        pass
    
    try:
        if s[0+1].isalpha():
            pass
        else:
            return False
    except IndexError:
        return False
    
    if s[2] == "0":
        return False
    else:
        pass
    
    prev_character = "1"
    for character in reversed(s[2:6]):
        if character.isdigit():
            if prev_character.isalpha():
                return False
        prev_character = character
        continue
        
    for character in s:
        if character in punctuation:
            return False
        
    else:
        return True
    
    
if __name__ == "__main__":
    main()