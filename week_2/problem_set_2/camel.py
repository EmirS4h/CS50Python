def camel_to_snake(camel_case: str) -> str:
    snake_case = ''
    for i, char in enumerate(camel_case):
        # If current character is uppercase, add an underscore before it
        if char.isupper() and i > 0:
            snake_case += '_'
        # Convert the character to lowercase and append to the result
        snake_case += char.lower()
    return snake_case


print(camel_to_snake(input("camelCase: ")))
