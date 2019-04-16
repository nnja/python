try:
    int("a")
except ValueError as error:
    print(f"Something went wrong. Message: {error}")

print("Reached end of the program.")