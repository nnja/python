# Lists are mutable
my_list = [1, 2, 3]
my_list[0] = 'a'
my_list

# Dictionaries are also mutable
my_dict = {"hello": "world"}
my_dict["foo"] = "bar"
my_dict

# Sets are mutable, but don't support
# indexing or item assignment,
# so you have to use add() and remove()
my_set = {1, 2, 3}
my_set[0] = 'a' # This will throw a TypeError
my_set.add('a')
my_set

# Tuples are immutable
my_tuple = (1, 2, 3)
my_tuple[0] = 'a' # This will throw a TypeError