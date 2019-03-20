def mystery():
    num = 10 * 3

    if num == 10:
        print("condition 10")
        num = num * 10
    elif num == 30:
        print("condition 30")
        num = num * 30

    print(f"num was {num}")
    return num

print(mystery())