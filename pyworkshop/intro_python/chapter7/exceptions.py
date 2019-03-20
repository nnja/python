# this will throw an error
try:
    int("a")
except ValueError as e:
    print("oops, you can't do that!", e)

print("this is the end of my program")