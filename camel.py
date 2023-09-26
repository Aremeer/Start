def main():
    s = input("")
    for c in s: #i looked this up in a hint
        if c == str.upper(c): #i looked up str functions on a https://iq.opengenus.org/
            print("_", str.lower(c), end="", sep="")
        else:
            print(c, end="") #i looked this up in a hint
    
main()