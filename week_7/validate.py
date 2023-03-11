import re

email = input("What's your email? ").strip()

# r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$"
if re.search(r"^\w+@(\w+\.)*\w+\.edu$", email, flags=re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")


# start from the beginning
# can have anything but a @ 1 or more times at least 1 required
# should have @
# after @ there needs to be at least 1 or more character that is not a @
# should end with .edu literally
# ^[^@]+@[^@]+\.edu$
