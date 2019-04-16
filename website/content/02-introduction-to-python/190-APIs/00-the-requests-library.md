---
title: "Using The Requests Library"
date: 2019-03-16T21:38:59-07:00
weight: 3
---

### What is The `requests` Library?

Python is "batteries included", but sometimes the included libraries available in the standard library can be hard to understand. The standard library focuses on functionality, but not necessarily ease of use.

That's where external libraries come in. The external `requests` library was developed by Kenneth Reitz to make working with APIs in Python a lot easier. He calls it "HTTP, for humans." It's become of the (if not the most) popular Python library!

### Our First Request With The `requests` Library

{{% notice tip %}}
If you didn't install the `requests` library in the working with libraries chapter, you'll need to do that first before running this code. Use: `python -m pip install requests`
{{% /notice %}}

Let's make a request to shibe.online to get ourselves some dog pictures. Create a file called `shibe.py` in our `pyworkshop` directory and copy this:

```python
# First thing we'll do is import the requests library
import requests

# Define a variable with the URL of the API
api_url = "http://shibe.online/api/shibes?count=1"

# Call the root of the api with GET, store the answer in a response variable
# This call will return a list of URLs that represent dog pictures
response = requests.get(api_url)

# Get the status code for the response. Should be 200 OK
# Which means everything worked as expected
print(f"Response status code is: {response.status_code}")

# Get the result as JSON
response_json = response.json()

# Print it. We should see a list with one image URL.
print(response_json)
```

```bash
(env) $ python shibe.py
Response status code is: 200
['https://cdn.shibe.online/shibes/28d7c372ea7defdb315ef845285d4ac3906ccea4.jpg']
```

### Dealing with Errors

When dealing with HTTP requests, your first indication of error is usually the HTTP status code. You saw some of the common status codes in the last chapter. The most common status codes are probably `200` - Success, and `404` - Not found. You can find the status code in the `status_code` property of the `response` object:

```python
# Passing in a non-existant URL will result in a 404 (not found)
bad_response = requests.get("http://shibe.online/api/german-shepards")
print(f"Bad Response Status Code is: {bad_response.status_code}")  # Status code is 404, meaning that resource doesn’t exist.
```

### Passing in Parameters

```python
# We'll store our base URL here and pass in the count parameter later
api_url = "http://shibe.online/api/shibes"

params = {
   "count": 10
}

# Pass those params in with the request.
api_response = requests.get(api_url, params=params)

print(f"Shibe API Response Status Code is: {api_response.status_code}")  # should be 200 OK

json_data = api_response.json()

print("Here is a list of URLs for dog pictures:")
for url in json_data:
    print(f"\t {url}")
```

```bash
$ shibe.py
Shibe API Response Status Code is: 200
Here is a list of URLs for dog pictures:
     https://cdn.shibe.online/shibes/dfb2af0b2ac1f057750da32f0ea0e154afc160cf.jpg
     https://cdn.shibe.online/shibes/4989daad2c805ec62b0fb09a80280ba2262f1b08.jpg
     https://cdn.shibe.online/shibes/a9360b8262c586af2cf53a2d68bb6ec34b87fe25.jpg
     https://cdn.shibe.online/shibes/a168cc7f2524c73b433afd7c02f698884738daff.jpg
     https://cdn.shibe.online/shibes/3fbe49908948718c521b756f31dc155ed22941f6.jpg
     https://cdn.shibe.online/shibes/846bb52389cf9af8a54eb12f48e0e7d0883b17da.jpg
     https://cdn.shibe.online/shibes/d11ed7f57c5a882f047b921a73f0b95714626bb3.jpg
     https://cdn.shibe.online/shibes/0fd1dcc9f5866cefaa3040de1be0f8971b0530cd.jpg
     https://cdn.shibe.online/shibes/cd668ca05d0ec78863f3c30b08b9cd4ff7f5669c.jpg
     https://cdn.shibe.online/shibes/32bf0797e5a4c5bfb6fc06edc57ddfbf4e08f98f.jpg
```

#### More about `requests`

To learn more about the `requests` library *after* class, look at the [quick start](http://docs.python-requests.org/en/master/user/quickstart/).
