""""
# Python code to find and print the square of each number in a list
numbers = [1, 2, 3, 4, 5]  # A list of numbers
squares = []  # Empty list to store squares

for number in numbers:
    squares.append(number ** 2)  # Append the square of each number to the list

print(squares)  # Output: [1, 4, 9, 16, 25]


# Python code to demonstrate variable assignment and data types
age = 30  # An integer assignment
height = 5.9  # A floating-point number
name = "Alex"  # A string
is_adult = age > 18  # A boolean expression

print(f"{name} is {age} years old and {height} feet tall. Adult? {is_adult}")
# Output: Alex is 30 years old and 5.9 feet tall. Adult? True

# List of mixed data types
mixed_list = [age, height, name, is_adult]
print(mixed_list)  # Output: [30, 5.9, 'Alex', True]


# A list of crayons
crayons = ["blue", "green", "yellow", "red"]

for crayon in crayons:
    if crayon == "blue":
        print("Color the sky with", crayon)
    elif crayon == "green":
        print("Color the grass with", crayon)
    else:
        print("Color the flowers with", crayon)

# This will tell you:
# Color the sky with blue
# Color the grass with green
# Color the flowers with yellow
# Color the flowers with red

"""

def greet(name, message="Hello"):
    """Function to greet someone with a custom message or a default message."""
    return f"{message}, {name}!"

# Using the function with a custom message
print(greet("Alice", "Welcome"))  # Output: Welcome, Alice!

# Using the function with the default message
print(greet("Bob"))  # Output: Hello, Bob!



# Non-Pythonic way: using a loop to create a list of squares
squares = []
for i in range(10):
    squares.append(i * i)

# Pythonic way: using list comprehension to create the same list
squares = [i * i for i in range(10)]

print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]




