def mystery():
    num = 10 * 3

    if num == 10:
        print("Num was equal to 10")
        num = num * 10
    if num == 20:
        print("Num was equal to 20")
        num = num * 20
    if num == 30:
        print("Num was equal to 30")
        num = num * 30

    print(f"Value of returned num is: {num}")
    return num

mystery()