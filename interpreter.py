def main():
    expression = input("Expression: ")
    list_exp = expression.split()
    if list_exp[1] == "/":
        result = int(list_exp[0]) / int(list_exp[2])
    elif list_exp[1] == "*":
        result = int(list_exp[0]) * int(list_exp[2])
    elif list_exp[1] == "-":
        result = int(list_exp[0]) - int(list_exp[2])
    elif list_exp[1] == "+":
        result = int(list_exp[0]) + int(list_exp[2])
        
    print(float(round(result, 2)))
    
main()