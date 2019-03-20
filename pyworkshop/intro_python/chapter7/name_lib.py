def upper_case_name(name):
    return name.upper()

if __name__ == "__main__":
    name = "Nina"
    name_upper = upper_case_name(name)
    print(f"Upper case name is {name_upper}")
    print("dunder name", __name__)