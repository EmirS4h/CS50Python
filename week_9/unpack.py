# first, _ = input("What's your name? ").split()
# print(f"Hello, {first}")


def total(galleons: int, sickles: int, knuts: int) -> int:
    return (galleons * 17 + sickles) * 29 + knuts


coins = [100, 50, 25]
print(total(*coins), "Knuts")

coins = {
    "sickles": 50,
    "knuts": 25,
    "galleons": 100,
}

print(total(**coins), "Knuts")


def topla(*numbers: tuple[int]):
    total = 0
    for n in numbers:
        total += n
    print(total)


topla(1, 2, 3, 4, 5)
