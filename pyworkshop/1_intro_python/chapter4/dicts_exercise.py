# Remember, dictionaries don't have numerical indexes
# like lists, so if you try to use an index number...
# Unless 0 happens to be a key.
my_dict = {"key": "value"}
my_dict[0]

my_dict["hello"] = "world"
my_dict["foo"] = "bar"
my_dict
my_dict["hello"]
my_dict.get("hello")
my_dict["baz"]
"baz" in my_dict
my_dict.get("baz", "boo")
my_dict.keys()
my_dict.values()
my_dict.items()
