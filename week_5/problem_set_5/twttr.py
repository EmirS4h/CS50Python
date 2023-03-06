def main():
    pass


def shorten(word: str) -> str:
    new_str = ""

    for ch in word:
        c = ch.lower()
        if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
            continue
        new_str += ch

    return new_str


if __name__ == "__main__":
    main()
