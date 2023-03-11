import re


def main():
    print(parse(input("HTML: ").strip()))


def parse(s: str) -> str | None:
    if matches := re.search(r"/embed/([\w]+)", s, flags=re.IGNORECASE):
        return f"https://youtu.be/{matches.group(1)}"
    return None


def get_srcs(s: str):
    matches = re.findall(r'src=[\'"]?([^\'" >]+)', s, flags=re.IGNORECASE)
    print(matches)


if __name__ == "__main__":
    main()
