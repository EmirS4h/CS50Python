inp = input("Input: ")
new_str = ""

for ch in inp:
    c = ch.lower()
    if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
        continue
    new_str += ch

print("Output:", new_str)
