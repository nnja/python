---
title: "Practice"
date: 2019-03-08T00:00:00-08:00
draft: false
weight: 70
pre: "<b>⭐️ </b>"
---

## Running Code

Let's create a basic program that we can run as a file on the command line. We'll start with a basic framework using a `main()` function.

```python
def main():
    pass

if __name__ == "__main__":
    main()
```

Save your file as `file_exercise.py` and run it from the command line using `python file_exercise.py`. Note: we are concentrating on Python 3 for this class, so if you have Python 2 installed, you may need to explicitly use `python3 file_exercise.py`.

What happened? Because you ran the file directly, the file's `__name__` variable is set to `__main__`, which triggers the `if` statement to run the `main()` function. This is a common pattern that you'll see in Python programs, and it comes in handy for being able to write programs that work both on their own and when imported into other programs. The `pass` keyword does nothing, it's just there to keep the empty `main()` function from throwing a syntax error.

Let's start filling in our `main()` function. We have a json file named `cities.json` which contains the top five cities in the US, sorted by population. You can [download `cities.json` here](/code/cities.json). Let's open the file and load in the data.

```python
import json

def main():
    cities_file = open("cities.json")
    cities_data = json.load(cities_file)
    print(cities_data)

if __name__ == "__main__":
    main()
```

First, we imported the built-in `json` library to help us decode the json file. Then, we opened the file using the `open()` function, and passed the open file handle to the `json.load()` function. The `load()` function read our data in and spit it out as a Python representation - in this case, a list of dictionaries. We then print this list.

{{%expand "Here's what you should have seen on your command line:" %}}

```bash
(env) $ python file_execise.py
[{'name': 'New York', 'pop': 8550405}, {'name': 'Los Angeles', 'pop': 3971883}, {'name': 'Chicago', 'pop': 2720546}, {'name': 'Houston', 'pop': 2296224}, {'name': 'Philadelphia', 'pop': 1567442}]
```

{{%/expand%}}

This list is a little hard to make sense of in its raw form, let's print it a little nicer. Use `enumerate()` to go through the list and print it nicely:

```python
import json

def main():
    cities_file = open("cities.json")
    cities_data = json.load(cities_file)

    print("Largest cities in the US by population:")

    for index, entry in enumerate(cities_data):
        print(f"{index + 1}: {entry['name']} - {entry['pop']}")

if __name__ == "__main__":
    main()
```

A few new things here: first, remember that `enumerate()` outputs a tuple of (index, entry), so we use `index` and `entry` variables to capture those. Then, for every item in the list, we print the index (+ 1, because zero-indexed lists are sometimes hard to read), and we pull the name and population out of each entry dictionary using the dictionary `[]` syntax.

{{%expand "Here's what you should have seen on your command line:" %}}

```bash
(env) $ python file_execise.py
Largest cities in the US by population:
1: New York - 8550405
2: Los Angeles - 3971883
3: Chicago - 2720546
4: Houston - 2296224
5: Philadelphia - 1567442
```

{{%/expand%}}

One more thing to clean up - using the `open()` keyword on its own is frowned upon, because it won't automatically close any resources you might open. Even if you call the `close()` keyword yourself, there's no guarantee your program won't crash, leaving important resources dangling. It's safer to open files inside a context using the `with` keyword. Once your code exits the scope of the context, your file is automatically closed. Note: our reading and formatting code has shifted to the right because of the change in scope.

```python
import json

def main():
    with open("cities.json") as cities_file:
        cities_data = json.load(cities_file)

        print("Largest cities in the US by population:")
        for index, entry in enumerate(cities_data):
            print(f"{index + 1}: {entry['name']} - {entry['pop']}")

    print("The file is now closed.")

if __name__ == "__main__":
    main()
```

{{%expand "Here's what you should have seen on your command line:" %}}

```bash
(env) $ python file_execise.py
Largest cities in the US by population:
1: New York - 8550405
2: Los Angeles - 3971883
3: Chicago - 2720546
4: Houston - 2296224
5: Philadelphia - 1567442
The file is now closed.
```

{{%/expand%}}

## Handling Exceptions

Parsing files - especially if you didn't create them - is often tricky, and you're going to have to deal with less-than-perfect data. For example, go into your `cities.json` file and delete the last `]` character. Run your program again.

{{%expand "Here's what you should have seen on your command line:" %}}

```bash
(env) $ python file_execise.py
Traceback (most recent call last):
  File "file_execise.py", line 14, in <module>
    main()
  File "file_execise.py", line 5, in main
    cities_data = json.load(cities_file)
  File "/usr/local/Cellar/python/3.7.2_2/Frameworks/Python.framework/Versions/3.7/lib/python3.7/json/__init__.py", line 296, in load
    parse_constant=parse_constant, object_pairs_hook=object_pairs_hook, **kw)
  File "/usr/local/Cellar/python/3.7.2_2/Frameworks/Python.framework/Versions/3.7/lib/python3.7/json/__init__.py", line 348, in loads
    return _default_decoder.decode(s)
  File "/usr/local/Cellar/python/3.7.2_2/Frameworks/Python.framework/Versions/3.7/lib/python3.7/json/decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "/usr/local/Cellar/python/3.7.2_2/Frameworks/Python.framework/Versions/3.7/lib/python3.7/json/decoder.py", line 353, in raw_decode
    obj, end = self.scan_once(s, idx)
json.decoder.JSONDecodeError: Expecting ',' delimiter: line 21 column 1 (char 234)
```

{{%/expand%}}

Helpfully, the library told you (on the last line) approximately what is wrong and where. It also provides a Traceback to help you see what happened, starting with your `main()` function, which called `json.load(cities_file)`, and into the functions used internally to the `json` library. This will become more useful once you start writing your own libraries, so practice reading and understanding your Tracebacks.

But let's say we're writing a web app or user-facing app and don't want our users to see Tracebacks (they can be scary if you're not a programmer, as well as risk your security by leaking information about your software). Let's catch that `JSONDecodeError` and return something prettier.

```python
import json

def main():
    with open("cities.json") as cities_file:
        try:
            cities_data = json.load(cities_file)

            print("Largest cities in the US by population:")
            for index, entry in enumerate(cities_data):
                print(f"{index + 1}: {entry['name']} - {entry['pop']}")

        except json.decoder.JSONDecodeError as error:
            print("Sorry, there was an error decoding that json file:")
            print(f"\t {error}")

    print("The file is now closed.")

if __name__ == "__main__":
    main()
```

Here, we've wrapped our business logic in another scope - the `try - except` block. For the `except`, we reach into the `json` library and reference the `JSONDecodeError` that's part of the `decoder` module. We assign it to `error` so that we can reference it later. We then print out the entire error, prefixed with a tab character `\t` to make it a little easier to read. Voilà, we've caught our error and reported it to the user with (hopefully) helpful information (but not too much information).

{{%expand "Here's what you should have seen on your command line:" %}}

```bash
(env) $ python file_execise.py
Sorry, there was an error decoding that json file:
	 Expecting ',' delimiter: line 21 column 1 (char 234)
The file is now closed.
```

{{%/expand%}}