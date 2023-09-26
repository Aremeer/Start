def main():
    greeting = input("Greeting: ").lower().lstrip() #found correct syntax https://www.w3schools.com/python/python_ref_string.asp
    if greeting[0:5] == "hello" : #found info how to use strirng slicing operator https://www.codingdeeply.com/how-to-get-first-letter-of-string-in-python/?expand_article=1
        print("$0")
    elif greeting[0] == "h":
        print("$20")
    else:
        print("$100")


main()