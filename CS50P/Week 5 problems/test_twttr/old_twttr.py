def main():
    #we take in a string of text
    #we turn it into a list
    #print each word again unles it's a vowel (A E I O U)
    vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
    txt = input("Input: ")
    print("Output: ", end="")
    for i in txt:
        if i in vowels:
            continue
        else:
            print(i, sep="", end="")
    print()





main()