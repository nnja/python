+++
title = "Practice"
date = 2019-01-25T15:07:04-06:00
weight = 200
draft = false
pre = "<b>⭐️ </b>"
+++

Let's review what we learned today and put it all together.

For the final exercise of today, we're going to write a small program that requests the top repositories from GitHub, ordered by the number of stars each repository has, then we're going to print the results to our terminal. Create a new file called `day_one.py`.

{{% notice note %}}
You may need to install the `requests` library using `python -m pip install requests`. You may see `pip` used directly, but using `python -m pip` is [recommended by Python](https://docs.python.org/3/installing/index.html).
{{% /notice %}}

Let's start with our key function, the one that gets the data from the [GitHub API](https://developer.github.com/v3/search/). Use the `requests` library to do a GET request on the GitHub search API URL ("https://api.github.com/search/repositories"). Use `if __name__ == "__main__"` to check to make sure we're running the file directly, and to call our function. Don't forget to `import requests`

{{%expand "You should have something like this:" %}}

```python
import requests

def repos_with_most_stars():
    gh_api_repo_search_url = "https://api.github.com/search/repositories"

    response = requests.get(gh_api_repo_search_url)

    print(response.text)


if __name__ == "__main__":
    repos_with_most_stars()
```

{{%/expand%}}


{{%expand "Here's what you should have seen on your command line:" %}}

```bash
(env) $ python day_one.py
{"message":"Validation Failed","errors":[{"resource":"Search","field":"q","code":"missing"}],"documentation_url":"https://developer.github.com/v3/search"}
```

{{%/expand%}}

### Getting a Response

Looks like we got a response from the GitHub API! Looks like we hit an error - we're missing search parameter. Checking the `documentation_url` that GitHub helpfully provides, we can see that we're missing the parameter `q`, which contains search keywords. Let's hardcode a query string to find repos with more than 50,000 stars and try again. We'll add our query string to the `parameters` dict as `q`, and pass it to the `params` argument of `requests.get()`

{{%expand "You should have something like this:" %}}

```python
import requests

def repos_with_most_stars():
    gh_api_repo_search_url = "https://api.github.com/search/repositories"

    parameters = {"q": "stars:>50000"}
    response = requests.get(gh_api_repo_search_url, params=parameters)

    print(response.text)


if __name__ == "__main__":
    repos_with_most_stars()
```

{{%/expand%}}

{{%expand "Here's what you should have seen on your command line:" %}}

```bash
(env) $ python day_one.py
{"total_count":33,"incomplete_results":false,"items":[{"id":28457823,"node_id":"MDEwOlJlcG9zaXRvcnkyODQ1NzgyMw==","name":"freeCodeCamp"...
```
{{%/expand%}}


### Response Parsing

Woah, we got a huge response from GitHub, including metadata for 33 repos. Let's parse it out so we can make better sense of what we have - use `response.json()` to get the returned data in json format. We see that GitHub returns a list called `items` in our response, so let's `return` that. Then, in your main function, loop through it and print out the important bits.

{{%expand "You should have something like this:" %}}

```python
import requests

def repos_with_most_stars():
    gh_api_repo_search_url = "https://api.github.com/search/repositories"

    parameters = {"q": "stars:>50000"}
    response = requests.get(gh_api_repo_search_url, params=parameters)
    response_json = response.json()

    return response_json["items"]


if __name__ == "__main__":
    results = repos_with_most_stars()

    for result in results:
        language = result["language"]
        stars = result["stargazers_count"]
        name = result["name"]

        print(f"-> {name} is a {language} repo with {stars} stars.")
```
{{%/expand%}}

{{%expand "Here's what you should have seen on your command line:" %}}

```bash
(env) $ python day_one.py
-> freeCodeCamp is a JavaScript repo with 298059 stars.
-> bootstrap is a JavaScript repo with 131410 stars.
-> vue is a JavaScript repo with 130168 stars.
-> react is a JavaScript repo with 124029 stars.
-> tensorflow is a C++ repo with 122328 stars.
-> free-programming-books is a None repo with 118241 stars.
-> awesome is a None repo with 103392 stars.
-> You-Dont-Know-JS is a None repo with 97587 stars.
...
```

{{%/expand%}}


### Narrowing it Down

We should now have a much more readable list of 33 or so repos, along with their number of stars. Let's narrow down our search a bit. To use multiple search keywords, we'll have to programatically construct our query string. Using the GitHub API documentation, let's make a new function to construct a query string for the repository search endpoint that searches for any number of languages, and limits our query to repos with more than 50,000 stars:

{{%expand "You should have something like this:" %}}

```python
def create_query(languages, min_stars=50000):
    # An example search query looks like:
    # stars:>50000 language:python language:javascript

    query = f"stars:>{min_stars} "

    for language in languages:
        query += f"language:{language} "

    return query
```

{{%/expand%}}


Now, let's call our new `create_query()` function from `repos_with_most_stars()`, replacing our hardcoded query string. Add a `languages` argument so that we can pass in a list of languages to use to create our query. Also add `sort` and `order` parameters, which we'll hardcode to "stars" and "desc" for now.

{{%expand "You should have something like this:" %}}

```python
def repos_with_most_stars(languages):
    gh_api_repo_search_url = "https://api.github.com/search/repositories"

    query = create_query(languages)
    sort = "stars"
    order = "desc"
    parameters = {"q": query, "sort": sort, "order": order}

    response = requests.get(gh_api_repo_search_url, params=parameters)
    response_json = response.json()

    return response_json["items"]
```

{{%/expand%}}

Finally, let's add a `languages` list to limit which languages we're interested in, and pass it to `repos_with_most_stars()`. Now, when we call our `repos_with_most_stars()` function with `["python", "javascript", "ruby"]` as our languages, the `create_query()` function will output create a query string that looks like `q=stars:>50000+language:python+language:javascript+language:ruby+&sort=stars&order=desc`. Because this is a simple GET request, this gets appended to our `gh_api_repo_search_url`, so our actual request URL is `https://api.github.com/search/repositories?q=stars:>50000+language:python+language:javascript+language:ruby+&sort=stars&order=desc`.

Run your program.

{{%expand "You should have something like this:" %}}

```python
if __name__ == "__main__":
    languages = ["python", "javascript", "ruby"]
    results = repos_with_most_stars(languages)

    for result in results:
        language = result["language"]
        stars = result["stargazers_count"]
        name = result["name"]

        print(f"-> {name} is a {language} repo with {stars} stars.")
```

{{%/expand%}}

{{%expand "Here's what you should have seen on your command line:" %}}

```bash
(env) $ python day_one.py
-> freeCodeCamp is a JavaScript repo with 298059 stars.
-> bootstrap is a JavaScript repo with 131410 stars.
-> vue is a JavaScript repo with 130169 stars.
-> react is a JavaScript repo with 124029 stars.
-> d3 is a JavaScript repo with 82945 stars.
-> javascript is a JavaScript repo with 82531 stars.
-> react-native is a JavaScript repo with 74828 stars.
-> create-react-app is a JavaScript repo with 64748 stars.
-> awesome-python is a Python repo with 63734 stars.
-> angular.js is a JavaScript repo with 59413 stars.
-> Font-Awesome is a JavaScript repo with 59051 stars.
-> system-design-primer is a Python repo with 58972 stars.
-> node is a JavaScript repo with 58863 stars.
-> axios is a JavaScript repo with 56121 stars.
-> public-apis is a Python repo with 53212 stars.
-> jquery is a JavaScript repo with 51040 stars.
```

{{%/expand%}}

### Cleaning Up and Handling Errors

Looking good, we now have a sorted list of the top python, javascript, and ruby repos. Let's do a little bit of clean up and error handling. We might not always want to sort by "stars" or order by "desc", so move those to keyword arguments. That way, they'll be good defaults, but if someone calling our `repos_with_most_stars` function wants to override them, they can.

{{%expand "You should have something like this:" %}}

```python
def repos_with_most_stars(languages, sort="stars", order="desc"):
    gh_api_repo_search_url = "https://api.github.com/search/repositories"

    query = create_query(languages)
    parameters = {"q": query, "sort": sort, "order": order}

    response = requests.get(gh_api_repo_search_url, params=parameters)
    response_json = response.json()

    return response_json["items"]
```

{{%/expand%}}

Next, we should handle any errors we might run into with the API. Maybe you've gotten one already. Let's add some basic error handling on the response's HTTP status code. We'll check for a `403`, a common error that GitHub uses to tell you that you're hitting their API too quickly, and `raise` and error. We'll also `raise` an error if the status code is anything but `200` (success).

{{%expand "You should have something like this:" %}}

```python
def repos_with_most_stars(languages, sort="stars", order="desc"):
    gh_api_repo_search_url = "https://api.github.com/search/repositories"
    query = create_query(languages)

    # Define the parameters we want to be part of our URL
    parameters = {"q": query, "sort": sort, "order": order}

    # Pass in the query and the parameters as part of the request.
    response = requests.get("https://api.github.com/search/repositories", params=parameters)
    status_code = response.status_code

    # Check if the rate limit was hit. Applies only for students running this code
    # in the in-person course.
    if status_code == 403:
        raise RuntimeError("Rate limit reached. Please wait a minute and try again.")
    if status_code != 200:
        raise RuntimeError(f"An error occurred. HTTP Status Code was: {status_code}.")
    else:
        response_json = response.json()
        records = response_json["items"]
        return records
```
{{%/expand%}}

There, your code should do the same thing, but should handle errors much better.

{{%expand "The final code, with additional comments, can be found here:" %}}


```python
"""
A small Python program that uses the GitHub search API to list
the top projects by language, based on stars.

GitHub Search API documentation: https://developer.github.com/v3/search/

Additional parameters for searching repos can be found here:
https://help.github.com/en/articles/searching-for-repositories#search-by-number-of-stars

Note: The API will return results found before a timeout occurs,
so results may not be the same across requests, even with the same query.

Requests to this endpoint are rate limited to 10 requests per
minute per IP address.
"""

import requests


def create_query(languages, min_stars=50000):
    """
    Create the query string for the GitHub search API,
    based on the minimum amount of stars for a project, and
    the provided programming languages.

    An example search query looks like:
    stars:>50000 language:python language:javascript
    """
    query = f"stars:>{min_stars} "

    for language in languages:
        query += f"language:{language} "

    return query


def repos_with_most_stars(languages, sort="stars", order="desc"):
    gh_api_repo_search_url = "https://api.github.com/search/repositories"
    query = create_query(languages)

    # Define the parameters we want to be part of our URL
    parameters = {"q": query, "sort": sort, "order": order}

    # Pass in the query and the parameters as part of the request.
    response = requests.get(gh_api_repo_search_url, params=parameters)
    status_code = response.status_code

    # Check if the rate limit was hit. Applies only for students running this code
    # in the in-person course.
    if status_code == 403:
        raise RuntimeError("Rate limit reached. Please wait a minute and try again.")
    if status_code != 200:
        raise RuntimeError(f"An error occurred. HTTP Status Code was: {status_code}.")
    else:
        response_json = response.json()
        records = response_json["items"]
        return records


if __name__ == "__main__":
    languages = ["python", "javascript", "ruby"]
    results = repos_with_most_stars(languages)

    for result in results:
        language = result["language"]
        stars = result["stargazers_count"]
        name = result["name"]

        print(f"-> {name} is a {language} repo with {stars} stars.")
```
{{%/expand%}}
