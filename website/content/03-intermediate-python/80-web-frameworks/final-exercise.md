+++
title = "Practice"
date = 2019-01-25T15:07:04-06:00
weight = 200
draft = false
pre = "<b>⭐️ </b>"
+++

### Installing Requirements

Our web application has two required external libraries, `flask`, and `requests`. As our list of dependencies becomes more complicated, we want to list them in a file called `requirements.txt` and include it with our project. That way, our code can be reused by others.

Open and look at the `requirements.txt` file. The name of each dependency is on a new line.

{{% notice note %}}
As you advance in your Python journey, you can use the more advanced [`pipenv`](https://pipenv.readthedocs.io/en/latest/) tool to handle complicated dependencies.
{{% /notice %}}

To install all the dependencies from our requirements file, pass the `-r` flag to `pip`, and the name of the file (in this case, it's `requirements.txt`):

```bash
(env)$ python -m pip install -r requirements.txt
```

### Review

Let's review what we learned over the last two days and put it all together.

For our final exercise today, we're going to build on yesterday's final exercise, where we wrote a program to query the GitHub API for a list of repos for certain programming languages, sorted by number of stars. We'll be turning yesterday's exercise into a Flask webapp. Flask is a simple and popular framework for creating basic web apps in Python.

First, create a new folder for this exercise, called `day_two_final`. You'll need two folders of static content - CSS and HTML files - to make this work. You can [download them here](https://learnpython.dev/code/day_two_final_exercise/static_files.zip). Unzip your `static_files.zip` file and copy your `static` and `template` folders to your `day_two_final` folder.

Next, create a folder called `repos`. This is where we'll create our custom module. Inside this folder we'll create three files: `exceptions.py`, `models.py`, and `api.py`.

In `exceptions.py`, we'll create a custom exception class to handle errors with the GitHub API.
In `models.py`, we'll create a `GitHubRepo` class to more easily represent the results from the GitHub API search.
And `api.py` will hold our functions for querying the GitHub API.

Finally, we'll add an `app.py` file in the root level, to run our Flask app. Your folder should look like this:

```text
day_two_final
├── app.py
├── repos
│   ├── exceptions.py
│   ├── models.py
│   └── api.py
├── static
│   ├── favicon.png
│   └── style.css
└── templates
    ├── error.html
    └── index.html
```

### `exceptions.py`

Let's start with building a custom exception to handle API errors. Remember that is `response.status_code` is anything but `200`, you can consider that an error. Create a `GitHubApiException` class that subclasses `Exception`. Have it accept a `status_code` argument, and use that to create a custom message (you can copy the error strings we used yesterday). Pass the message to `Exception`

{{%expand "You should have something like this:" %}}

```python
class GitHubApiException(Exception):

    def __init__(self, status_code):
        if status_code == 403:
            message = "Rate limit reached. Please wait a minute and try again."
        else:
            message = f"HTTP Status Code was: {status_code}."

        super().__init__("A GitHub API Error Occurred: " + message)
```

{{%/expand%}}


### `models.py`

Next, let's build our "model", the `GitHubRepo` class. For this, we want to accept three arguments (`name`, `language`, and `num_stars`) and store them as instance variables (using `self`). To have a user-friend way to print our repo information, add a `__str__()` method that prints a message with the three repo parameters. For completeness, see if you can add a `__repr__()` method that returns the Python code needed to recreate this object.

{{%expand "You should have something like this:" %}}

```python
class GitHubRepo:

    def __init__(self, name, language, num_stars):
        self.name = name
        self.language = language
        self.num_stars = num_stars

    def __str__(self):
        return f"-> {self.name} is a {self.language} repo with {self.num_stars} stars."

    def __repr__(self):
        return f'GitHubRepo({self.name}, {self.language}, {self.num_stars})'
```

{{%/expand%}}


### `api.py`

In our `api.py` file, we're going to copy in our `create_query()` function and the `repos_with_most_stars()` function from yesterday.

In `create_query()`, see if you can clean up the code a little by replacing the `for` loop with a string join that accepts a list comprehension.

Clean up your `repos_with_most_stars()` function by using `raise` to throw your `GitHubAPIException` if the `status_code` does not equal `200`. Then, instead of returning items directly from the response json, see if you can use a list comprehension to create and return a list of `GitHubRepo` objects.

Don't forget to import your `GitHubApiException`, your `GitHubRepo` class, and the `requests` module.

{{%expand "You should have something like this:" %}}

```python
from repos.exceptions import GitHubApiException
from repos.models import GitHubRepo
import requests
GITHUB_API_URL = "https://api.github.com/search/repositories"

def create_query(languages, min_stars):
    """
    Create the query string for the GitHub search API,
    based on the minimum amount of stars for a project, and
    the provided programming languages.
    """
    # Notice we are calling .strip() on each language, to clear it of leading
    # and trailing whitespace
    query = " ".join(f"language:{language.strip()}" for language in languages)
    query = query + f" stars:>{min_stars}"
    return query

def repos_with_most_stars(languages, min_stars=40000, sort="stars", order="desc"):
    query = create_query(languages, min_stars)
    parameters = {"q": query, "sort": sort, "order": order}
    print(parameters)
    response = requests.get(GITHUB_API_URL, params=parameters)

    if response.status_code != 200:
        raise GitHubApiException(response.status_code)

    response_json = response.json()
    items = response_json["items"]
    return [GitHubRepo(item["name"], item["language"], item["stargazers_count"]) for item in items]
```

{{%/expand%}}


### `app.py`

Finally, let's tie it all together with our `app.py` file. We'll start off with some boilerplate - we'll need to import a few things from `flask`, as well as our `GitHubApiException` and our `repos_with_most_stars()` function:

```python
from flask import Flask, render_template, request

from repos.exceptions import GitHubApiException
from repos.api import repos_with_most_stars
```

Next, we'll create the flask `app` object. We'll also create a list of all the available languages that the user of our web app can choose from. It will help us keep track of if they're selected or not.

```python
app = Flask(__name__)

available_languages = ["Python", "JavaScript", "Ruby", "Java"]
```


Next, we'll need a function that gets called when the root url for our website, or `/` is requested by the user

. We'll start with the `@app.route()` decorator - we didn't cover decorators in this class, but just know that this signals to Flask that this `index()` function should be called to handle any `GET` or `POST` requests to the URL `/`.

```python
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        # code for a GET
        pass
    elif request.method == 'POST':
        # code for a POST
        pass
```


We need to figure out which languages we have selected to determine which repos to display.

We'll check the `request.method` variable to determine what kind of request it was - if it was a `GET` request, we'll just display whichever repos were selected last (or all of them if this is the first request).

If it's a `POST`, we'll grab the `languages` variable from the request form and use it to populate our `selected_languages` list:

```python
    if request.method == 'GET':
        # Use the list of all languages
        selected_languages = available_languages
    elif request.method == 'POST':
        # Use the languages we selected in the request form
        selected_languages = request.form.getlist("languages")
```

Now, we just need to get our results and render our website. Call the `repos_with_most_stars()` function in `api.py` and pass it our `selected_languages`.

Then, we'll return our flask `render_template()` function and pass it our list of selected languages, available languages, and our results.

```python
    results = repos_with_most_stars(selected_languages)

    return render_template(
        'index.html',
        selected_languages=selected_languages,
        available_languages=available_languages,
        results=results)
```

Finally, we'll add a custom error handler renders a special website (`error.html`) if we receive a `GitHubApiException`:

```python
@app.errorhandler(GitHubApiException)
def handle_api_error(error):
    return render_template('error.html', message=error)
```

Phew.
{{%expand "Here's the final `app.py` file that you should have:" %}}

```python
from flask import Flask, render_template, request

from repos.api import repos_with_most_stars
from repos.exceptions import GitHubApiException

app = Flask(__name__)

available_languages = ["Python", "JavaScript", "Ruby", "Java"]


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        # Use the list of all languages
        selected_languages = available_languages
    elif request.method == 'POST':
        # Use the languages we selected in the request form
        selected_languages = request.form.getlist("languages")

    results = repos_with_most_stars(selected_languages)

    return render_template(
        'index.html',
        selected_languages=selected_languages,
        available_languages=available_languages,
        results=results)


@app.errorhandler(GitHubApiException)
def handle_api_error(error):
    return render_template('error.html', message=error)

```

{{%/expand%}}


### Run your Webapp

At last, make sure you're in your root `day_two_final` directory `$ cd day_two_final` and start your webapp with debug mode.

```bash
(env) $ export FLASK_ENV=development; python3 -m flask run
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 165-366-879
```

Point your web browser to the given URL (http://127.0.0.1:5000/ in this case) and you should see your list of repos sorted by number of stars. Play with the check boxes and the submit button on the left and see how the repo list changes. Congrats, you wrote a webapp in Python!


### Bonus: Unit Tests

Let's add some quick unit tests to our code, to make sure we don't introduce any regressions later on. Create a file called `test.py` in your `day_two_final` folder. Your folder should look like this:

```text
day_two_final
├── app.py
├── test.py
├── repos
│   ├── exceptions.py
│   ├── models.py
│   └── api.py
├── static
│   ├── favicon.png
│   └── style.css
└── templates
    ├── error.html
    └── index.html
```

Create a new `unittest.TestCase` called `TestCreateQuery`. Inside, make a method called `test_create_query()`. In this method, create a list of language names and an `int` representing the a minimum number of stars. By looking at the `create_query()` function, see if you can figure out what the correct query string should be. Call the `create_query()` function with your test variables and use `self.assertEqual()` to make sure they match. Don't forget to `import repos.api` and add your `unittest.main()` invocation.

{{%expand "You should have something like this:" %}}
```python
import repos.api
import unittest

class TestCreateQuery(unittest.TestCase):

    def test_create_query(self):
        test_languages = ["Python", "Ruby", "Java"]
        test_min_stars = 10000

        expected = "language:Python language:Ruby language:Java stars:>10000"
        result = repos.api.create_query(test_languages, test_min_stars)

        self.assertEqual(result, expected, "Unexpected result from create_query")

if __name__ == "__main__":
    unittest.main()
```
{{%/expand%}}

Run your test:

{{%expand "Here's what you should have seen on your command line:" %}}

```bash
$ python test.py --verbose
test_create_query (__main__.TestCreateQuery) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

{{%/expand%}}

Let's make two more quick tests of our GitHubApiException. Make a new `TestCase` with two test functions. Name the class and functions using the same naming convention we've been using. For the first, we'll use a fake `status_code` of `403`. Create a `GitHubApiException` object and pass it the `status_code`. Check to see if the string "Rate limit" exists in the string representation of your exception (hint: use `str()`).

For the second test, we'll do the same thing with a `status_code` of `500`. This time, we'll check to see if "500" exists in the exception string.

{{%expand "You should have something like this:" %}}

```python
import repos.api
import repos.exceptions
import unittest

class TestCreateQuery(unittest.TestCase):

    def test_create_query(self):
        test_languages = ["Python", "Ruby", "Java"]
        test_min_stars = 10000

        expected = "language:Python language:Ruby language:Java stars:>10000"
        result = repos.api.create_query(test_languages, test_min_stars)

        self.assertEqual(result, expected, "Unexpected result from create_query")

class TestGitHubApiException(unittest.TestCase):

    def test_exception_403(self):
        status_code = 403
        exception = repos.exceptions.GitHubApiException(status_code)
        self.assertTrue("Rate limit" in str(exception), "'Rate limit' not found")

    def test_exception_500(self):
        status_code = 500
        exception = repos.exceptions.GitHubApiException(status_code)
        self.assertTrue(str(status_code) in str(exception))

if __name__ == "__main__":
    unittest.main()
```

{{%/expand%}}

{{%expand "Here's what you should have seen on your command line:" %}}

```bash
$ python test.py --verbose
test_create_query (__main__.TestCreateQuery) ... ok
test_exception_403 (__main__.TestGitHubApiException) ... ok
test_exception_500 (__main__.TestGitHubApiException) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

{{%/expand%}}
