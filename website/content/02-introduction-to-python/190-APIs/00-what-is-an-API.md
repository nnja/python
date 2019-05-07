---
title: "What Is an API?"
date: 2019-03-16T21:38:31-07:00
draft: false
weight: 1
---

Per the dictionary, an API is:

> a set of functions and procedures allowing the creation of applications that access the features or data of an operating system, application, or other service.

An API is a standardized way of accessing information across the web, between clients and servers. These days most APIs are *RESTful*. That means they follow a common set of paradigms and practices.

There are many types of APIs, but these days they're commonly known to refer to *web* APIs.

#### Authentication

Some, but not all APIs require you to authenticate. Methods of authentication are out of the scope of this class, but you'll be happy to know that there are plenty of free APIs available that require no authentication at all.

#### Rate Limiting

Some APIs allow unauthenticated requests, but they're usually *rate limited*. Rate limiting means prevent the same client (usually by IP address) from making too many requests at once and overloading the server. *The GitHub API allows 50 unauthenticated requests per hour per IP, or 10 unauthenticated requests to their Search API.*

Note: After the class, you can find a detailed list of APIs in this [public-apis repo](https://github.com/toddmotto/public-apis).

#### Free APIs

{{% notice note %}}
Free APIs are... free. That means that they may go down if their owner decides to drop their upkeep. If the API used in these examples doesn't work in the future, try a different one listed in the `public-apis` repo linked to above.
{{% /notice %}}

