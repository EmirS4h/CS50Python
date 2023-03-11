import re

name = input("What's your name? ").strip()

if matches := re.search(r"^(.+), *(.+)$", name):
    name = f"{matches.group(2)} {matches.group(1)}"


# if matches:
#     name = f"{matches.group(2)} {matches.group(1)}"
print(f"hello, {name}")
