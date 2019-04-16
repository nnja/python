---
title: "Anatomy of a Python Program"
date: 2019-03-08T23:25:07-08:00
draft: false
weight: 4
---

Let's take a very quick look at a Python program that uses the GitHub Search API to display a list of popular repositories in three different programming languages, sorted by the amount of stars that they have. It may be hard to believe, but by the end of the day, you'll be able to write a program just like this.

### A Python program for using the GitHub search API

```python
"""
A small Python program that uses the GitHub search API to list
the top projects by language, based on stars.
"""

import requests

GITHUB_API_URL = "https://api.github.com/search/repositories"


def create_query(languages, min_stars=50000):
    query = f"stars:>{min_stars} "

    for language in languages:
        query += f"language:{language} "

    # a sample query looks like: "stars:>50 language:python language:javascript"
    return query


def repos_with_most_stars(languages, sort="stars", order="desc"):
    query = create_query(languages)
    params = {"q": query, "sort": sort, "order": order}

    response = requests.get(GITHUB_API_URL, params=params)
    status_code = response.status_code

    if status_code != 200:
        raise RuntimeError(f"An error occurred. HTTP Code: {status_code}.")
    else:
        response_json = response.json()
        return response_json["items"]


if __name__ == "__main__":
    languages = ["python", "javascript", "ruby"]
    results = repos_with_most_stars(languages)

    for result in results:
        language = result["language"]
        stars = result["stargazers_count"]
        name = result["name"]

        print(f"-> {name} is a {language} repo with {stars} stars.")
```

### Step by step

{{%expand "Expand this section to walk through the program step-by-step." %}}

There's some helpful information about the program in a comment at the top. The comment is separated with triple quotes `"""`.

The first thing we're doing is importing the popular `requests` library. We'll be using it to make API calls.

```python
import requests
```

Next, we define the URL for the GitHub search API, which we found in the documentation for that endpoint in a variable called `GITHUB_API_URL`. This variable is named in all upper case because it's a constant. A value that we don't expect to change over the course of our program.

```python
GITHUB_API_URL = "https://api.github.com/search/repositories"
```

First, the code in the `main` method will run. This code defines three different languages we'd like to see results for.

```python
    languages = ["python", "javascript", "ruby"]
```

Then calls the `repos_with_most_stars` method with that language list, and gets back a list of results.

```python
    results = repos_with_most_stars(languages)
```

Let's jump to the `repos_with_most_stars` function. We know it's a function because of the `def` keyword, followed by a function name, parameters -- both required and optional in parenthesis, and finally, a colon `:`. It accepts a list of languages to sort by, as well as some *optional* parameters for how we want to sort the list. By default, we sort it by the number of stars the repo has, in descending order.

```python
def repos_with_most_stars(languages, sort="stars", order="desc"):
```

Next, we need to create a query string that this particular API understands. We do that in the `create_query` function. This function takes the languages as a required parameter, and the minimum number of stars we'd like to query for as an optional parameter.

```python
def create_query(languages, min_stars=50000):
```

In this function, we create a query string that looks like this `stars:>50000 language:python language:javascript language:ruby". These parameters of this query string are defined by the expectations of the API that we're working with. We return this value.

Since the query is a little confusing, there's a comment in the code that explains what it does. The comment starts with `# `.

Back in the `repos_with_most_stars` function, we use our query string as part of the parameters that we'll be passing in to the API, along with the URL that we'll be using.

We declare them in a dictionary called `params`, like this:

```python
# looks like: q=stars:>50000+language:python+language:javascript+language:ruby+&sort=stars&order=desc'
params = {"q": query, "sort": sort, "order": order}
```

These params map to part of a URL that will look like this: `q=stars:>50000+language:python+language:javascript+language:ruby+&sort=stars&order=desc`

Next, we use these parameters as well as the URL defined in `GITHUB_API_URL` to call the API using the requests library.

```python
    response = requests.get("https://api.github.com/search/repositories", params=params)
```

We're requesting the data at this URL: [https://api.github.com/search/repositories?q=stars:>50000+language:python+language:javascript+language:ruby+&sort=stars&order=desc](https://api.github.com/search/repositories?q=stars:>50000+language:python+language:javascript+language:ruby+&sort=stars&order=desc)

We're using the requests library because it allows us to quickly and easily work with the data returned from an API.

Next, we quickly check the HTTP status code to make sure that it was 200. If it wasn't, that means that something went wrong with our request and we'll want to throw an exception to quit our program.

```python
    if status_code != 200:
        raise RuntimeError(f"An error occurred. HTTP Code: {status_code}.")
```

If everything went OK, we get the JSON from the response as a Python dictionary, using `response.json()`, next, we `return` the data in the "items" key back to the main method. In this case, we don't care about the additional data that the API returned.

```python
        response_json = response.json()
        return response_json["items"]
```


Next, back in the main method, we go through each result, and print out a line with the name of the repo, the language, and the amount of stars it has.

```python
        print(f"-> {name} is a {language} repo with {stars} stars.")
```

{{% /expand %}}


### End Result

The end result looks something like this:

```bash
(env) $ python dayone.py

-> freeCodeCamp is a JavaScript repo with 298046 stars.
-> bootstrap is a JavaScript repo with 131403 stars.
-> vue is a JavaScript repo with 130099 stars.
-> react is a JavaScript repo with 123969 stars.
-> d3 is a JavaScript repo with 82932 stars.
-> javascript is a JavaScript repo with 82514 stars.
-> react-native is a JavaScript repo with 74810 stars.
-> create-react-app is a JavaScript repo with 64725 stars.
-> awesome-python is a Python repo with 63693 stars.
... and more results
```

{{% notice note %}}
Don't worry if you didn't understand this code, we'll be building this program in the workshop today.
{{% /notice %}}