x = "Hello, {name}!"
print(x.format(name="Alice"))  # Output: Hello, Alice!
print(x.format_map(("name""Bob")))  # Output: Hello, Bob!
