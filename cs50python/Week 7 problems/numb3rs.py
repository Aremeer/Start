import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.match(r"(?:[1-9]|[1-9][0-9]|[1][0-9][0-9]|[2][0-4][0-9]|[2][5][0-5])\.(?:(?:[0-9]|[1-9][0-9]|[1][0-9][0-9]|[2][0-4][0-9]|[2][5][0-5])\.){2}(?:[0-9]|[1-9][0-9]|[1][0-9][0-9]|[2][0-4][0-9]|[2][5][0-5])$", ip):
        return True
    else:
        return False


#https://www3.ntu.edu.sg/home/ehchua/programming/howto/Regexe.html
if __name__ == "__main__":
    main()