def name_length(name):
    return len(name)

def upper_case_name(name):
    return name.upper()

def lower_case_name(name):
    return name.lower()

name = "Nina"
length = name_length(name)
upper_case = upper_case_name(name)

print(f"The length is {length} and the uppercase version is: {upper_case}")
# print(f"The value of __name__ is: {__name__}")