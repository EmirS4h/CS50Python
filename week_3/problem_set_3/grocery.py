groceries = {}

while True:
    try:
        item = input()
        groceries[item] = groceries.get(item, 0) + 1
    except EOFError:
        for k, v in groceries.items():
            print(f"{v} {k.upper()}")
        break
    except KeyboardInterrupt:
        for k, v in groceries.items():
            print(f"{v} {k.upper()}")
        break
