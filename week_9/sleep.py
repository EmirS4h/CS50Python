def main():
    n = int(input("What's n? "))
    for i in sheep(n+1):
        print(i)


# def sheep(n: int):
#     return ["🐑" * i for i in range(n)]

def sheep(n: int):
    for i in range(n):
        yield "🐑" * i


if __name__ == "__main__":
    main()
