class Vehicle:

    def __init__(self, make, model, fuel="gas"):
        self.make = make
        self.model = model
        self.fuel = fuel

daily_driver = Vehicle("Subaru", "Crosstrek")
# By default, this is how python represents our object:
print(daily_driver)

# The variables we saved to the instance are available like this:
print(f"I drive a {daily_driver.make} {daily_driver.model}. It runs on {daily_driver.fuel}.")
