def main():
    camelCase = input("camelCase: ")
    print("snake_case: ", end="")
    for i in camelCase:
        if i.isupper():
            print("_", str.lower(i), end="", sep="")
        else:
            print(i, end="")
    print("")

main()