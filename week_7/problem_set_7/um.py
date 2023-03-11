import re


def main():
    print(count("wow um fk um"))
    print(count("wow yumm"))
    print(count("wow um"))
    print(count("wow um,           um      umumum"))
    print(count("wow um.            um.    uma"))


def count(s: str) -> int:
    return len(re.findall(r"(?<!\w)um(?!\w)", s, flags=re.IGNORECASE))


if __name__ == "__main__":
    main()
