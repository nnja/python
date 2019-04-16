---
title: "Basic Flask"
date: 2019-03-10T19:30:36-07:00
draft: false
weight: 1
---

### Types of Web Frameworks in Python

#### Django

Django is a full-featured, high-level framework for building web apps. Django focuses on automating as much as possible, and many large-scale sites run on Django.


#### Flask

Flask is a "microframework" for Python, allowing users to make basic backend APIs and webapps with a minimum of code. Flask is easy for beginners and not opinionated, so we'll be focusing on it for today's exercises.

{{% notice note %}}
There are many more different frameworks for Python. You can find a more detailed list [here](https://wiki.python.org/moin/WebFrameworks).
{{% /notice %}}

#### Pyramid

Pyramid is a fast, yet advanced framework, and a successor to the older Pylons framework. Pyramid is open-source and actively developed.


## A Basic Flask App

{{% notice note %}}
Make sure you have Flask installed: `python -m pip install flask`
{{% /notice %}}

A very basic Flask app looks something like this:

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
```

First, we import `flask`, and create the `app` object using the name of the file (`__name__`). We add a route using `@app.route("/")` above our `hello()` function - this tells Flask to respond to requests for "/" (the root of your webserver) by running `hello()` and returning "Hello World!" to the user.

To run this, you could copy this code into a file called `hello.py`, set the `FLASK_APP` environment variable, and run it. Then just point your browser to the URL it gives you.

```bash
$ FLASK_APP=hello.py flask run
 * Running on http://localhost:5000/
```

### Routing

![](/03-intermediate-python/80-web-frameworks/images/request-response.jpeg?width=40pc)
<sub>Image from [Zapier Guide to APIs](https://zapier.com/learn/apis/chapter-1-introduction-to-apis/).</sub>

Flask uses the `route()` decorator to declare routes. For example, the above code uses `app.route("/")` to declare a route for "/" that resolves to `hello()`, but you can use any path, or even accept variables in your routes:

```python
@app.route("/my/secret/page")
def secret():
    return "Shh!"

@app.route("/user/<username>")
def user_page(username):
    return f"Welcome, {username}!"

@app.route("/blog/post/<int:post_id>")
def show_post(post_id):
    return f"This is the page for post # {post_id}"
```

More information about routing can be found in the [Flask documentation](http://flask.pocoo.org/docs/1.0/quickstart/#routing).

### Returning Data

The simplest way to return data is to return a string with `return` at the end of your function. This pushes the string back to the user, who sees it as plain text in their browser. You'll probably want to make use of HTML in your webapps though, so you'll want to look at template rendering.

A template is just an HTML file that lives in a folder called `templates` next to your flask app Python file. To return an HTML file instead of plain text, just return the `render_template()` function. For example:

```python
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')
```

Flask also supports a template language called `Jinja` that allows you to populate your HTML files with data from your Flask app at render time. A very simple HTML template might look like this:

```html
<!doctype html>
<title>Hello from Flask</title>
{% if name %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello, World!</h1>
{% endif %}
```

Notice the special code in `{% brackets %}`, this acts as a very simple programming language. Let's add a matching Flask function:

```python
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
```

Now, if we call `/hello`, we'll see `Hello, World!`, and if we call `/hello/nina`, we'll see `Hello nina!`. This is a very simple example, you can find more details in the [Flask documentation](http://flask.pocoo.org/docs/1.0/quickstart/#rendering-templates) and the [Jinja documentation](http://jinja.pocoo.org/docs/2.10/templates/).


### Static Files

Serving static files alongside your dynamic Flask code is easy - just create a folder called `static` next to your Flask code, and any files you put in there will be available at `/static/<your filename>`.


### Debug Mode

Flask has a very handy built-in debugger that makes it very easy to see what went wrong when you have an error in your application. You can activate the debugger by setting the `FLASK_ENV` variable:

```bash
$ export FLASK_APP=my_application
$ export FLASK_ENV=development
$ flask run
```

### Using a Database

Flask provides a useful mechanism for accessing database objects. This makes it easy to use databases to store data for your dynamic webapp. More information is available in the [Flask documentation](http://flask.pocoo.org/docs/1.0/tutorial/database/).

### Deploying your Web App

Is your app ready for the big time? There are many different options for deploying your Flask app to a real webserver - you can read about some of your options in the [Flask documentation](http://flask.pocoo.org/docs/1.0/deploying/#deployment).

#### More About Flask

{{% notice note %}}
We'll be covering just the basics of `flask` today. To deep dive and learn more, the [`flask` Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) is a great resource to check out *after* class.
{{% /notice %}}