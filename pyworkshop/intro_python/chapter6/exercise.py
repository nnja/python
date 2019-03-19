# if, elif, else

def test_number(number):
    if number < 100:
        print("This is a pretty small number")
    elif number == 100:
        print("This number is alright")
    else:
        print("This number is huge!")
test_number(5)
test_number(99)
test_number(100)
test_number(8675309)

# multiple conditions

def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizzbuzz!")
fizzbuzz(3)
fizzbuzz(5)
fizzbuzz(15)

# Truthiness

def my_func(my_list):
    if my_list:
        for item in my_list:
            if item is None:
                print("Got None!")
            else:
                print(item)
    else:
        print("Got an empty list!")
my_func([1, 2, 3])
my_func([2, None, "hello", 42])
my_func([])

# For loop, range, enumerate

my_list = [0, 1, 2]
for num in my_list:
    print(f"Next value: {num}")

for num in range(0, 3):
    print(f"Next value: {num}")

my_list = ["foo", "bar", "baz"]
for index, item in enumerate(my_list):
    print(f"Item {index}: {item}")

# dictionary keys
my_dict = {"foo": "bar", "hello": "world"}
for key in my_dict:
    print(f"Key: {key}")
for key in my_dict.keys():
    print(f"Key: {key}")

# dictonary values
for value in my_dict.values():
    print(f"Value: {value}")

# most commonly used: dictionary items
for key, value in my_dict.items():
    print(f"Item {key} = {value}")

# break, continue, return
# break
for num in range(0, 100):
    print(f"Testing number {num}")
    if num == 3:
        print("Found number 3!")
        break
    print("Not yet...")

# continue
for num in range(0, 100):
    print(f"Testing number {num}")
    if num < 3:
        continue
    elif num == 5:
        print("Found number 5!")
        break
    print("Not yet...")

# return
def is_number_in_list(number_to_check, list_to_search):
    for num in list_to_search:
        print(f"Checking {num}...")
        if num == number_to_check:
            return True
    return False
my_list = [1, 2, 3, 4, 5]
is_number_in_list(27, my_list)
is_number_in_list(2, my_list)

# while loop
counter = 0
while counter < 3:
    print(f"Counter = {counter}")
    counter += 1

counter = 0
while True:
    print(f"Counter = {counter}")
    if counter == 3:
        break
    counter += 1

# nested loop
names = ["Rose", "Max", "Nina"]
target_letter = 'x'
found = False

for name in names:
    for char in name:
            if char == target_letter:
                    found = True
                    break

    if found:
        print(f"Found {name} with letter: {target_letter}")
        break

for x in range(0, 5):
    for y in range(0, 5):
        print(f"x = {x}, y = {y}")
        if y == 2:
            break