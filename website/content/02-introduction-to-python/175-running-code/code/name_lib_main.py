def name_length(name):
    return len(name)

def upper_case_name(name):
    return name.upper()

def lower_case_name(name):
    return name.lower()

if __name__ == "__main__":
    name = "Nina"
    length = name_length(name)
    upper_case = upper_case_name(name)

    print(f"The length is {length} and the uppercase version is: {upper_case}")