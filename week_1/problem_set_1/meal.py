def main():
    time = convert(input("What time is it? "))
    if time >= 7.00 and time <= 8.00:
        print("breakfast time")
    elif time >= 12.00 and time <= 13.00:
        print("lunch time")
    elif time >= 18.00 and time <= 19.00:
        print("dinner time")


def convert(time: str) -> str:
    h, m = time.split(":")
    return float(h) + (float(m) / 60)


main()
