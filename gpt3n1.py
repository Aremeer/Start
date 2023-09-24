def process_number(n):
    while n > 1:
        if n % 2 != 0:  # If the number is odd
            print(n)  # Display the current number
            n = (n * 3) + 1  # Divide by 3 and add 1
        else:  # If the number is even
            print(n)  # Display the current number
            n = n // 2  # Divide by 2
    print(n)  # Display the final number

# Input a starting number
starting_number = int(input("Enter a starting number: "))
process_number(starting_number)
