def main():
    print_block(4, 2)


def print_column(height: int):
    print("#\n"*height, end="")


def print_row(width: int):
    print("?"*width, end="")


def print_square(size: int):
    for _ in range(size):
        print("#"*size)


def print_block(width: int, height: int):
    for _ in range(height):
        print("#"*width)


main()
