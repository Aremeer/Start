#Functions
    #Functions are verbs or actions that the computer or computer language will already know how to perform.
    
    len #lenght of a list in numbers
        students = ["Hermione", "Harry", "Ron"]
    
        for i in range(len(students)):
            print(i, students[i])

#Arguments
    name(x, y, z) # in this case x, y, z would be arguments

#Variables
        name, x, i ect. #A variable is just a container for a value within your own program.
            name = input("What's your name? ")
            print("hello," name)


#Comments
    #Comments are a way for programmers to track what they are doing in their programs and even inform others about their intentions for a block of code. In short, they are notes for yourself and others that will see your code!
        # Ask the user for their name


#Pseudocode
        # Ask the user for their name
        name = input("What's your name? ")

        # Print hello
        print("hello,")

        # Print the name inputted
        print(name)


#Strings and Paremeters
    str #A string, known as a str in Python, is a sequence of text.
    #Looking at this documentation, you’ll learn that the print function automatically include a piece of code end='\n'. This \n indicates that the print function will automatically create a line break when run. The print function takes an argument called end` and the default is to create a new line.

        # Ask the user for their name
        name = input("What's your name? ")
        print("hello,", end="")
        print(name)


#Formatting Strings
    (f"x" {y}) #Probably the most elegant way to use strings would be as follows:

        # Ask the user for their name
        name = input("What's your name? ")
        print(f"hello, {name}")

    #Notice the f in print(f"hello, {name}"). This f is a special indicator to Python to treat this string a special way, different than previous approaches we have illustrated in this lecture. Expect that you will be using this style of strings quite frequently in this course.
    

#More on Strings
    #You should never expect your user will cooperate as intended. Therefore, you will need to ensure that the input of your user is corrected or checked.
    
    strip #By utilizing the method strip on name as name = name.strip(), it will strip all the whitespaces on the left and right of the users input. You can modify your code to be:
        name = name.strip()

    title #Using the title method, it would title case the user’s name:
        nname = name.title()
        
    #We could even go further!
        name = input("What's your name? ").strip().title()


#Loops
    while #loop
        number = get_number()
        meow(number)


        def get_number():
            while True:
                n = int(input("What's n? "))
                if n > 0:
                break
            return n
        
    for #loop
        students = ["Hermione", "Harry", "Ron"]
    
        for student in students:
            print(student)


#= sign has a special role in programming. This equal sign literally assigns what is on the right to what is on the left.