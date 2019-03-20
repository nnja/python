class Vehicle:

    def __init__(self, make, model, fuel="gas"):
        self.make = make
        self.model = model
        self.fuel = fuel


class Car(Vehicle):

    number_of_wheels = 4


class Truck(Vehicle):

    number_of_wheels = 6

    def __init__(self, make, model, fuel="diesel"):
        super().__init__(make, model, fuel)


daily_driver = Car("Subaru", "Crosstrek")
print(f"I drive a {daily_driver.make} {daily_driver.model}. "
      f"It uses {daily_driver.fuel} and has {daily_driver.number_of_wheels} wheels.")

truck = Truck("Ford", "F350")
print(f"I also have a {truck.make} {truck.model}. "
      f"It uses {truck.fuel} and has {truck.number_of_wheels} wheels.")

print(
    f"My daily driver is a {type(daily_driver)} and my truck is a {type(truck)}")

print(f"Is my daily driver a car? {isinstance(daily_driver, Car)}")
print(f"Is my truck a Vehicle? {isinstance(truck, Vehicle)}")
print(f"Is my truck a Car? {isinstance(truck, Car)}")

print(f"Is a Truck a subclass of Vehicle? {issubclass(Truck, Vehicle)}")
