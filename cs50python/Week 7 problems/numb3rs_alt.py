import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip):
        checked_ip = []
        ip = ip.split(".")
        for match in ip:
            if int(match) >= 0 and int(match) <= 255:
                checked_ip.append(match)
        if checked_ip == ip:
            return True
        else:
            return False   
    else:
        return False

#https://www3.ntu.edu.sg/home/ehchua/programming/howto/Regexe.html
if __name__ == "__main__":
    main()