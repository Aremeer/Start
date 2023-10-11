import re
import sys


#im not greedy https://stackoverflow.com/questions/2503413/regular-expression-to-stop-at-first-match

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r'src="https?://(?:www.)?youtube\.com/embed/(.*?)"', s):
        return f"https://youtu.be/{matches.group(1)}"
    else:
        return None


if __name__ == "__main__":
    main()