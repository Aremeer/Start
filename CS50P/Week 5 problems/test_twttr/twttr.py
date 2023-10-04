def main():
    twttr = shorten(list(input("Input: ")))
    print(twttr)



def shorten(text):
    vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
    twttr = str()
    for letter in text:
        if letter in vowels:
            pass
        else:
            twttr = twttr + letter
    return twttr
            


if __name__ == "__main__":
    main()

    
    

