# Part 1

10 > 5
5 > 10
10 > 10
10 >= 10
5 < 10
5 < 5
5 <= 5
5 == 5
5 != 10

# Part 2

5 == True
# The number 5 does not equal True, but...
if 5:
    print("The number 5 is truthy!")
# The number 5 is truthy for an if test!

# Part 3

1 == True
0 == False

# Part 4

True or False
[] or [1, 2, 3]
"Hello" or None

True and False
5 and 0
[1] and [1, 2, 3]
"Hello" and None

# Of course, you can use `and` and `or` aren't limited to two operands
a = False
b = False
c = False
a or b or c
b = True
a or b or c
a and b and c
a = True
c = True
a and b and c
