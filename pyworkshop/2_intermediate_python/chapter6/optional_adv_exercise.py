#!/usr/bin/env python3

"""
A small command line Python program that uses the GitHub search API to list
the top projects by language, based on stars.

GitHub Search API documentation: https://developer.github.com/v3/search/

Requests to this endpoint are rate limited to 10 requests per
minute per IP address.
"""

import sys
import requests


GITHUB_API_URL = "https://api.github.com/search/repositories"


class GitHubApiException(Exception):

    def __init__(self, status_code):
        if status_code == 403:
            message = "Rate limit reached. Please wait a minute and try again."
        else:
            message = f"HTTP Status Code was: {status_code}."

        super().__init__("A GitHub API Error Occurred: " + message)


class GitHubRepo:
    """
    A class used to represent a single GitHub Repository.
    """

    def __init__(self, name, language, num_stars):
        self.name = name
        self.language = language
        self.num_stars = num_stars

    def __str__(self):
        return f"-> {self.name} is a {self.language} repo with {self.num_stars} stars."

    def __repr__(self):
        return f'GitHubRepo({self.name}, {self.language}, {self.num_stars})'


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


def repos_with_most_stars(languages, min_stars=50000, sort="stars", order="desc"):
    query = create_query(languages, min_stars)
    parameters = {"q": query, "sort": sort, "order": order}
    response = requests.get(GITHUB_API_URL, params=parameters)

    if response.status_code != 200:
        raise GitHubApiException(response.status_code)

    response_json = response.json()
    items = response_json["items"]
    return [GitHubRepo(item["name"], item["language"], item["stargazers_count"]) for item in items]


if __name__ == "__main__":
    # Accept an optional argument for minimum number of stars from the command line
    # $ ./gh_api 100000    # means an input of 100,000 minimum stars.
    script_arguments = sys.argv
    min_stars = 50000

    if len(script_arguments) >= 2:
        try:
            min_stars = int(script_arguments[1])
        except ValueError:
            sys.exit("Error: Command line argument must be a valid number.")

    # Accept the list of languages from the user, or provide a default list.
    languages = input(
        "Enter a comma separated list of programming languages (or press ENTER for defaults): "
        ).strip()
    if not languages:
        languages = ["python", "javascript", "ruby"]
    else:
        languages = languages.split(",")

    # Get the results
    result_repos = repos_with_most_stars(languages=languages, min_stars=min_stars)
    if not result_repos:
        print("No Results Found.")
    else:
        for repo in result_repos:
            print(repo)
