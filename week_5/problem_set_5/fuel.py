while True:
    try:
        x, _, z = input().split(' ')
        fraction = int(int(x) / int(z) * 100)
        if fraction >= 99:
            print("F")
        elif fraction <= 1:
            print("E")
        else:
            print(f"{fraction}%")
        break
    except ValueError:
        print("Cannot convert value/s to integer")
    except ZeroDivisionError:
        print("Cannot divide by zero")


def convert(fraction: str) -> int:
    x, y = fraction.split("/")
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        print("Cannot convert value/s to int")
    if x > y:
        raise ValueError
    if y == 0:
        raise ZeroDivisionError
    return int(int(x) / int(y) * 100)


def gauge(percentage: int) -> str:
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    return f"{percentage}%"
