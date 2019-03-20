try:
    my_dict = {"hello": "world"}
    print(my_dict["foo"])
except KeyError:
    print("Oh no! That key doesn't exist")

try:
    my_dict = {"hello": "world"}
    print(my_dict["foo"])
except KeyError as key_error:
    print(f"Oh no! The key {key_error} doesn't exist!")