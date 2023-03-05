def convert(inp: str) -> str:
    return inp.replace(":)", "🙂").replace(":(", "🙁")


def main():
    print(convert(input()))


main()
