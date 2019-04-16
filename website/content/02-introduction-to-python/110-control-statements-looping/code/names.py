names = ["Jimmy", "Rose", "Max", "Nina", "Phillip"]

for name in names:
    if len(name) != 4:
        continue

    print(f"Hello, {name}")

    if name == "Nina":
        break

print("Done!")
