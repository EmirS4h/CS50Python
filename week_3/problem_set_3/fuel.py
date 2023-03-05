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
