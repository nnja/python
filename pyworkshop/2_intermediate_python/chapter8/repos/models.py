"""
GitHub API Application: Custom Model Classes
"""

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
