import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    try:
        findall = re.findall(r"(\W|^)um(\W|$)", s, re.IGNORECASE)
        return len(findall)
    except:
        raise IndexError

if __name__ == "__main__":
    main()