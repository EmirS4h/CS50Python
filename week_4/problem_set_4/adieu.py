import inflect

p = inflect.engine()
names = []
while True:
    text = "Adieu, adieu, to "
    try:
        name = input("Name: ")
        names.append(name)
        text += p.join(names)
        print(text)
    except KeyboardInterrupt:
        break
