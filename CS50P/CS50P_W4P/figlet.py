#https://pypi.org/project/pyfiglet/0.7/
import sys
import random
from pyfiglet import Figlet
figlet = Figlet()


def main():
    
    if len(sys.argv) == 2:
        print("Invalid usage")
        sys.exit(1)
    if len(sys.argv) > 3:
        print("Invalid usage")
        sys.exit(1)
    if len(sys.argv) == 3:
        if sys.argv[1] not in ("-f", "--font"):
            print("Invalid usage")
            sys.exit(1)    
        fonts = []
        for font in figlet.getFonts():
            fonts.append(font)
        if sys.argv[2] not in fonts:
            print("Invalid usage")
            sys.exit(1)
    inputTxt = input("Input: ")
    if len(sys.argv) == 1:
        fonts = []
        for font in figlet.getFonts():
            fonts.append(font)
        f = Figlet(font=f"{random.choice(fonts)}")
    else:
        f = Figlet(font=f"{sys.argv[2]}")
    print(f.renderText(inputTxt))





if __name__ == "__main__":
    main()