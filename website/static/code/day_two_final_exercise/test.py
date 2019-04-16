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
