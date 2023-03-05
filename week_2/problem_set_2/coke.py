amount_due = 50
coin = 0

while amount_due > 0:
    print("Amount Due:", amount_due)
    coin = int(input("Insert Coin: "))
    amount_due -= coin

print("Change Owed:",coin - amount_due)
