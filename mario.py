def main():
    print_square()

def print_square():
    height = min(int(input("Input height: ")), 10)
    width = min(int(input("Input width: ")), 20)  # Adjusted width to be at most 10 times the height
    
    for _ in range(height):
        print("#" * width)

    
main()