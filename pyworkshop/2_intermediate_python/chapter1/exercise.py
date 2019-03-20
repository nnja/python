my_string = str(100)
my_string
type(my_string)

my_int = int(my_string)
print(my_int)
type(my_int)

float("3.1415")
int(3.1415)

# Converting between lists and strings
my_list = list("hello")
print(my_list)
str(my_list)

# String join method
''.join(my_list)
','.join(my_list)
'-'.join(my_list)

# String split
my_string = "the,quick,brown,fox"
my_string.split(",")

