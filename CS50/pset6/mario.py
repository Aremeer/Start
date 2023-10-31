def main():
    i = int(input("Height: "))
    for x in range(i):
        for _ in range(i - x - 1):
            print(" ", end="")
        for _ in range(x + 1):
            print("#", end="")
        print("  ", end="")
        for _ in range(x + 1):
            print("#", end="")
        print("")
        
if __name__ == "__main__":
    main()