import random


def main():
    secret_number = generate_integer(get_level())
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 1:
                continue
            if guess > secret_number:
                print("Too large!")
                continue
            elif guess < secret_number:
                print("Too small!")
                continue
            else:
                print("Just right!")
                break
        except ValueError:
            pass


def get_level() -> int:
    while True:
        try:
            level = int(input("Level: "))
            if level < 1:
                continue
            return level
        except ValueError:
            pass


def generate_integer(n: int) -> int:
    return random.randint(1, n)


if __name__ == "__main__":
    main()
