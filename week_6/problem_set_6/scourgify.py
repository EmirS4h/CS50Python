import csv
import sys


def main():
    args = sys.argv
    if len(args) == 3:
        before_name, after_name = args[1:]
        new_data = read_csv_data(before_name)
        write_csv_data(after_name, new_data, ["first", "last", "house"])
    elif len(args) < 2:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")


def read_csv_data(path_to_file: str) -> list[dict]:
    new_data: list[dict] = []
    try:
        with open(path_to_file, "r") as file:
            for row in csv.DictReader(file):
                last, first = row["name"].split(",")
                house = row["house"]
                new_data.append({
                    "first": first.lstrip(),
                    "last": last,
                    "house": house
                })
            return new_data
    except OSError:
        sys.exit("Could not read", path_to_file)


def write_csv_data(file_name: str, data: list[dict], headers: list[str]):
    try:
        with open(file_name, "w") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
    except OSError:
        sys.exit("Could not write to file", file_name)


if __name__ == "__main__":
    main()
