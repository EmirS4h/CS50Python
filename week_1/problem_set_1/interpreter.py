x, y, z = input().strip().split(' ')

x = int(x)
z = int(z)

match y:
    case "+":
        print(f"{float(x + z)}")
    case "-":
        print(f"{float(x - z)}")
    case "*":
        print(f"{float(x * z)}")
    case "/":
        if z == 0:
            print("Cannot divide by 0")
        else:
            print(f"{float(x / z):.1f}")
