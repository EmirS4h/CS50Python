import argparse


def main():
    # sets()
    # global_vs_local()
    account = Account()
    print(f"Balance: {account.balance}")
    account.deposit(100)
    account.withdraw(50)
    print(f"Balance: {account.balance}")


# houses.py
def sets():
    students = [
        {"name": "Hermione", "house": "Gryffindor"},
        {"name": "Harry", "house": "Gryffindor"},
        {"name": "Ron", "house": "Gryffindor"},
        {"name": "Draco", "house": "Slytherin"},
        {"name": "Padma", "house": "Ravenclaw"},
    ]
    houses = set()  # doesnt allow duplicates
    for student in students:
        houses.add(student["house"])
    print(houses)


# Bank.py
balance = 0


def global_vs_local():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)


def deposit(n):
    global balance
    balance += n


def withdraw(n):
    global balance
    balance -= n


class Account:
    def __init__(self, starting_balance: int = 0):
        self._balance = starting_balance

    def __str__(self):
        ...

    @property
    def balance(self):
        return self._balance

    def deposit(self, n: int):
        self._balance += n

    def withdraw(self, n: int):
        self._balance -= n


# Meows.py

def meow(n: int) -> str:
    return "meow\n" * n


if __name__ == "__main__":
    # main()
    # number: int = int(input("Number: "))
    # meows: str = meow(number)
    # print(meows, end="")
    parser = argparse.ArgumentParser(description="Meow like a cat")
    parser.add_argument("-n", default=1, type=int,
                        help="Number of times to meow")
    args = parser.parse_args()

    for _ in range(args.n):
        print("meow")
