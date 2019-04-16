---
title: "PyPI"
date: 2019-03-10T19:17:03-07:00
draft: false
weight: 5
---

PyPI (the Python Package Index) is an awesome service that helps you find and install software developed and shared by the Python community. Almost every user-contributed Python package has been published to PyPI. You can browse the site at [pypi.org](https://pypi.org/) but most of the time you will probably interact with it through Python's `pip` tool.

### Basic Usage

You can use the `pip` tool to install the latest version of a module and its dependencies from the Python Packaging Index:

```bash
(env) $ python -m pip install SomePackage
```


### Know your Packages

There are a lot of packages on PyPI, and they're not always up-to-date. Sometimes it helps to look at a package before installing it. Simply search for a package name on PyPI.org - for example, here's the page for the [redis package](https://PyPI.org/project/redis/). If you follow the Homepage link, you'll be taken to the project's [GitHub page](https://github.com/andymccurdy/redis-py), where you can see that the latest commit was very recently. So you know this package is actively maintained, and will probably work in your up-to-date version of Python.

{{% notice warning %}}
When you're first starting out, it's a good idea to copy the `pip install` text from the website, otherwise bad actors could take advantage of your typos.
{{% /notice %}}


We'll practice installing a package in the exercise for this chapter.