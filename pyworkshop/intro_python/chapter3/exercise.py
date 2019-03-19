# Part 1 - Basic Functions

def add_numbers(x, y):
    return x + y


add_numbers(1, 2)
print(f"The product of 1 and 2 is {add_numbers(1, 2)}")

# Function Scope
x = 1
y = 2

def add_numbers(x, y):
    print(f"Inside the function, x = {x} and y = {y}")
    return x + y

print(f"Outside the function, x = {x} and y = {y}")
print(f"The product of 5 and 6 is {add_numbers(5, 6)}")

# Positional vs Keyword Arguments
def calculate_numbers(x, y, operation="add"):
    if operation == "add":
        return x + y
    elif operation == "subtract":
        return x - y
calculate_numbers(2, 3)
calculate_numbers(2, 3, "subtract")
calculate_numbers(2, 3, operation="subtract")