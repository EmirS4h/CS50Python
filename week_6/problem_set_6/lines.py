import sys


def main():
    if len(sys.argv) == 2:
        if sys.argv[1].endswith(".py"):
            print(number_of_lines(sys.argv[1]))
        else:
            sys.exit("Not a Python file")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")


def number_of_lines(file_path: str) -> int:
    num = 0
    try:
        with open(file_path) as file:
            for line in file.readlines():
                if line.lstrip().startswith("#") or line == "\n":
                    continue
                num += 1
    except FileNotFoundError:
        sys.exit("File was not found")
    return num


if __name__ == "__main__":
    main()
