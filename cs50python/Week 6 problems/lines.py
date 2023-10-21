import sys

lines = []

def main():
    name = sys.argv
    if len(name) > 2:
        exit(1)
    elif ".py" not in name[1]:
        exit(1)
    try:
        with open(str(sys.argv[1])) as file:
            for line in file:
                x = line.strip()
                if line.isspace():
                    continue
                elif x[0] == "#":
                    continue
                else:
                    lines.append(line)
    except FileNotFoundError:
        exit(1)
    
    print(len(lines))


if __name__ == "__main__":
    main()