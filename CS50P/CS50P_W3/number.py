def main():
    x = get_int(input("What's x? "))
    print(f"x is {x}")



def get_int(input_str):
    while True:
        try: input_integer = int(input_str)
        except ValueError: print("The Value is not an integer")
        else: break
    return input_integer
        
        
        
main()