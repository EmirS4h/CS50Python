def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n: int) -> int:
    return n * n


if __name__ == "__main__":
    main()
