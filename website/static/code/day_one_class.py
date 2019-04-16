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

GITHUB_API_URL = "https://api.github.com/search/repositories"


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
    query = create_query(languages)

    # Define the parameters we want to be part of our URL
    parameters = {"q": query, "sort": sort, "order": order}

    # Pass in the query and the parameters as part of the request.
    response = requests.get(GITHUB_API_URL, params=parameters)
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
