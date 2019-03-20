while True:
    for divisor in range(5, -1, -1):
        try:
            quotient = 10 / divisor
            print(f"10 / {divisor} = {quotient}")
        except ZeroDivisionError:
            print("Oops! We tried to divide by zero!")
            raise RuntimeError