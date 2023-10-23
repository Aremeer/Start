from colorama import Fore, Back, Style



x = {"value":123}



print(Fore.RED + str(x["value"]))
print(Style.RESET_ALL, end="")