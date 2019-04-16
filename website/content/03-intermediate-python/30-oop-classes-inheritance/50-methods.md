---
title: "Methods"
date: 2019-03-10T19:29:24-07:00
draft: false
weight: 5
---

You've just seen the difference between class and instance variables. Classes can also have class methods - methods that are shared among all instances of a certain type. As with variables, they can be overriden in a specific instance or subclass.

Let's add a class method to our Car class:

```python
class Car:
    runs = True
    number_of_wheels = 4

    @classmethod
    def get_number_of_wheels(cls):
        return cls.number_of_wheels

    def start(self):
        if self.runs:
            print("Car is started. Vroom vroom!")
        else:
            print("Car is broken :(")
```

And call it:

```python
>>> my_car = Car()
>>> print(f"Cars have {Car.get_number_of_wheels()} wheels.")
Cars have 4 wheels.
# Of course, we can override this in our instance:
>>> my_car.number_of_wheels = 6
# And when we access our new instance variable:
>>> print(f"My car has {my_car.number_of_wheels} wheels.")
My car has 6 wheels.
# But, when we call our class method on our instance:
>>> print(f"My car has {my_car.get_number_of_wheels()} wheels.")
My car has 4 wheels.
```

Why? Because `get_number_of_wheels()` is a class method, and when it's called, the *class* (Car) gets passed in, and the value of `Car.number_of_wheels` is returned. Although we can access the instance variable (with a value of 6), the `get_number_of_wheels()` class method still returns the class variable, which is 4.


## `type`, `isinstance`, and `issubclass`

Python comes with some built-in functions for inspecting classes and types:

As we've seen throughout the workshop, the `type()` function returns the type of the object you pass it, or it's class. For example:

```python
>>> type(42)
<class 'int'>
>>> type("Hello world!")
<class 'str'>
>>> type(my_car)
<class '__main__.Car'>
```

The `isinstance()` function takes an object and a class, and returns `True` if the object you pass it is an instance of the class. For example:

```python
>>> isinstance(42, int)
True
>>> isinstance("Hello world!", str)
True
>>> isinstance(my_car, float)
False
>>> isinstance(my_car, Car)
True
```

The `issubclass` function takes two classes, and returns `True` if the first class is a subclass of the second. For example:

```python
# bool is a subclass of int
>>> issubclass(bool, int)
True
# int is a subclass of object
>>> issubclass(int, object)
True
# technically, everything is a subclass of object
>>> issubclass(bool, object)
True
```


### `__init__`

Classes can have an optional magic method called `__init__()` that gets run when you instantiate an instance of a class. You can use the `__init__()` method to do any special thing you want to happen when your instance is instantiated, including setting instance variables. `__init__` can take arguments, too.

{{% notice note %}}
Methods that are bracketed by underscores are sometimes called "magic methods." We won't be covering magic methods in this class, but we will point out a few of the interesting ones.
{{% /notice %}}

For example:

```python
class Car:
    runs = True

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        if self.runs:
            print(f"Your {self.make} {self.model} is started. Vroom vroom!")
        else:
            print(f"Your {self.make} {self.model} is broken :("
```

```python
>>> my_car = Car("Ford", "Thunderbird")
>>> my_car.start()
Your Ford Thunderbird is started. Vroom vroom!
```

Here, we accept two required variables, `make` and `model` in our `__init__()` method, and set instance variables of the same names using `self`. Later, when we call `start()`, we can grab `self.make` and `self.model` from the bound instance and use them in our string.


### `__str__` and `__repr__`

Classes have two other magic methods that come in handy for debugging, `__str__()` and `__repr__()`. Both functions return a string representation of an object. `__str__()` should return readable end-user output, and `__repr__()` should return the Python code necessary to rebuild the object. `__str__()` maps to the built-in function `str()` and `__repr__()` maps to the built-in function `repr()`.

For example, we'll use the `datetime` library to generate a `datetime` object for right now:

```python
>>> import datetime
>>> now = datetime.datetime.now()
>>> str(now)
'2019-03-16 21:04:01.396256'
>>> repr(now)
'datetime.datetime(2019, 3, 16, 21, 4, 1, 396256)'
```

You can see that `str()` has returned a human-readable date/time, and `repr()` has returned a string that represents the Python code we would need to run to recreate this object.

We can, of course, set our own `__str__()` and `__repr__()` methods in our custom classes:

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self):
        return f"<<Car object: {self.make} {self.model}>>"

    def __repr__(self):
        return f"Car('{self.make}', '{self.model}')"
```

```python
>>> my_car = Car("Ford", "Thunderbird")
>>> print(f"This object is a {str(my_car)}")
This object is a <<Car object: Ford Thunderbird>>
>>> print(f"To reproduce it, type: {repr(my_car)}")
To reproduce it, type: Car('Ford', 'Thunderbird')
```

### Bonus

You don't have to instantiate everything by hand, you can instantiate objects in `for` loops or even comprehensions. This is useful for running a function on a list of objects. For example, to convert a list of number-strings into a list of integers, you could do:

```python
>>> my_ints = [int(str_num) for str_num in ["1", "2", "3"]]
>>> print(my_ints)
[1, 2, 3]
```