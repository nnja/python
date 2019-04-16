---
title: "Working with APIs"
date: 2019-03-16T21:38:49-07:00
draft: false
weight: 2
---

{{% notice note %}}
Zapier has an *excellent* intro to APIs by by Brian Cooksey. The images and diagrams used on this page is from his post. Please read it [here](https://zapier.com/learn/apis/chapter-1-introduction-to-apis/).
{{% /notice %}}


### Requests and Responses

Working with APIs using HTTP depends on the request and response cycle. You send a request to the server, and it lets you know if your request was successful or by sending an HTTP Status Code with a special meaning, and will optionally send back data.

![](/02-introduction-to-python/190-APIs/images/request-response.jpeg?width=40pc)

### HTTP Methods

The HTTP Method (or verb) is how you tell the server which *type* of operation you'd like to perform.

- `GET` - Ask the server to get a resource.
- `POST` - Ask the server to create a resources, with the data that you've provided.
- `PUT` - Edit or update a resource.
- `DELETE` - Delete a resource.

### Headers, Body, Parameters

We can add additional to our request through headers, a body or URL parameters.

For today, we'll only be using URL parameters. They look like `https://example.com?var1=foo&var2=bar`.

### Response Types

Servers can respond in a variety of file formats, like JSON, XML, and others.

These days, JSON is the most common format. For many servers, it's the default if you don't specify a response type.

JSON is a common format of capturing data, and it's easy to read and generate from a variety of programming languages.

A JSON example:

```json
[
	{
		"name": "New York",
		"pop": 8550405
	},
	{
		"name": "Los Angeles",
		"pop": 3971883
	},
	{
		"name": "Chicago",
		"pop": 2720546
	},
	{
		"name": "Houston",
		"pop": 2296224
	},
	{
		"name": "Philadelphia",
		"pop": 1567442
	}
]
```


### HTTP Status Codes

HTTP Status Codes is a numerical response from the sever, indicating the status of your request.

They tend to fall into these categories:

- **`1xx` : Informational**
    - Not commonly used.
- **`2xx` : Success**
    - **`200 OK`** - Standard response for successful HTTP requests.
    - **`201 CREATED`** - A new resource was created successfully.
- **`3xx` : Redirection**
    - **`301 Moved Permanently`** - This and all future requests should be directed to the new URL.
- **`4xx` : A Client Error**
    - **`404 Not Found`** - An entry wasn't found based on the information the client gave.
- **`5xx` : A Server Error**
    - **`500 Internal Server Error`** - Something went wrong with the server.\


#### Because HTTP Status Codes are boring, we can try to remember them with cats instead!

| code                            	| cat                                                                                       	|
|---------------------------------	|-------------------------------------------------------------------------------------------	|
| **`200: OK`**                   	| ![](/02-introduction-to-python/190-APIs/images/200.jpeg?classes=shadow&outline&width=20pc) 	|
| **`301 Moved Permanently`**     	| ![](/02-introduction-to-python/190-APIs/images/301.jpeg?classes=shadow&outline&width=20pc) 	|
| **`404 Not Found`**             	| ![](/02-introduction-to-python/190-APIs/images/404.jpeg?classes=shadow&outline&width=20pc) 	|
| **`500 Internal Server Error`** 	| ![](/02-introduction-to-python/190-APIs/images/500.jpeg?classes=shadow&outline&width=20pc) 	|

<sub>Provided by [this awesome API](https://http.cat/).</sub>

#### Easter Egg - I'm a Teapot

One of my favorite bits of internet trivia is that in 1998 as an April fool's joke, HTTP Status Code `418 I'm a teapot`, a.k.a the Hyper Text Coffee Pot Control Protocol was implemented. You can pass the `BREW` command to it, to signal starting brewing a cup of coffee.

![](/02-introduction-to-python/190-APIs/images/Htcpcp_teapot.jpg?classes=shadow&outline&width=30pc)

### Authentication

There are several ways of authenticating to APIs, but they are out of the scope of this class.

To learn more about authentication, visit:

- (Concepts) Zapier - [Authentication Part 1](https://zapier.com/learn/apis/chapter-4-authentication-part-1/) and[Authentication Part 2](https://zapier.com/learn/apis/chapter-5-authentication-part-2/)  by Brian Cooksey
- Using [authentication in the `requests` library](http://docs.python-requests.org/en/master/user/authentication/) documentation.