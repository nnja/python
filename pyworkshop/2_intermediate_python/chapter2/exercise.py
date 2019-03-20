# Comprehensions
my_list = [num for num in range(0, 100) if num % 2 == 0]
print(my_list)

import random
my_dict = {num:random.randint(0, 100) for num in my_list}
print(my_dict)

my_set = {num for num in my_dict.values()}
print(my_set)

# Slicing
my_list = [num for num in range(0, 100)]
my_slice = my_list[30:70:2]
print(my_slice)

my_backwards_slice = my_slice[::-1]
print(my_backwards_slice)

# Zip
names = ["Nina", "Max", "Floyd", "Lloyd"]
scores = [random.randint(0, 100) for name in names]
print(scores)

for name, score in zip(names, scores):
    print(f"{name} got a score of {score}")

