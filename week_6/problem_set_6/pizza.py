import sys
import csv
from tabulate import tabulate


def main():
    if len(sys.argv) == 2:
        if sys.argv[1].endswith(".csv"):
            print(tabulate(read_menu(sys.argv[1]),
                  headers='keys', tablefmt="grid"))
        else:
            sys.exit("Not a CSV file")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")


def read_menu(path_to_menu: str) -> list:
    with open(path_to_menu) as file:
        return [row for row in csv.DictReader(file)]


if __name__ == "__main__":
    main()
