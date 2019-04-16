---
title: "Working With Python"
draft: false
weight: 3
---

{{% notice info %}}
Once we open our first Python file in VS Code, we'll see some configuration pop-ups. For the time being, **don't** dismiss them.
{{% /notice %}}

![Python Pop Ups](/01-introduction/02-requirements/05-vs-code/images/popups.png?classes=shadow,border)

## Configuring VS Code for Python

### Open the `project.py` file

If you haven't created a `project.py` file in the `pyworkshop` directory, now is the time to do so.
You can make a new file (Ctrl+N or ⌘P) and then save it (Ctrl+S or ⌘S).

Now that you've learned the necessary keyboard shortcuts, use Quick Open with `Ctrl+P` or `⌘P` to open the `project.py` file.

{{% notice info %}}
If you haven't installed the Python extension at this point, you'll get a pop-up recommending you install it for this type of file. Please [install it now](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=pyclass-docs-ninaz), and reload VS Code when prompted to load the extension.
{{% /notice %}}

## Configuring The Interpreter

Many operating systems include Python, but unfortunately it's usually a few versions behind.

We _never_ want to use Python2 for new Python projects, and we want to make sure we select the latest version of Python3 that we installed in the pre-requisites.

Luckily, VS Code is smart. If you launch it from a directory with an *activated* virtual environment, it'll automatically pick up the correct interpreter.

{{%expand "In case you need to configure the interpreter manually, follow these (optional) instructions." %}}

Click on the Select Python Interpreter button in the popup.

![Interpreter 1](/01-introduction/02-requirements/05-vs-code/images/interpreter.1.png?classes=shadow,border)


{{%expand "Note: If dismissed the popup, open the command palette and select Python: Select Interpreter. Expand this section for more details." %}}
![Interpreter 2](/01-introduction/02-requirements/05-vs-code/images/interpreter.2.png?classes=shadow,border)
{{% /expand%}}

Select the version of Python 3 in your virtual environment `env` folder as your interpreter. If you open a Python file in a new directory, you may need to select your interpreter again.

{{% /expand%}}

{{% notice tip %}}
You can always see what your interpreter is set to on the left side of the status bar at the bottom of the window.
{{% /notice %}}

![Selected Interpreter](/01-introduction/02-requirements/05-vs-code/images/selected-interpreter.png?classes=shadow,border)

## Setting Up a Linter

Per the [VS Code documentation](https://code.visualstudio.com/docs/python/linting?WT.mc_id=pyclass-docs-ninaz), linting highlights syntactical and stylistic problems in your Python source code. A linter will give you code hints about a variety of different types of problems. For example, when you have subtle errors in your code, like trying to use a variable you haven't defined yet. A linter will also show you when you're not following Python style convention called PEP8. PEP8 is a set of defined rules for how Python code should look. We'll cover it in more depth later, but what you need to know right now is that PEP8 warnings are not syntax errors. If your code doesn't adhere to the PEP8 standard, it will still run.

By default the linter will run every time you save a file, so it's good practice to save often with (Ctrl+S or ⌘S).

Let's go ahead and click install on the Linter popup.

![Install pylint](/01-introduction/02-requirements/05-vs-code/images/install-pylint.png?classes=shadow,border)

{{%expand "Note: If you accidentally dismissed the popup, open the command palette and search for Python: Select Linter, then select pylint. The popup will now reappear, and you can hit install. Expand this section for more details." %}}
![Select linter](/01-introduction/02-requirements/05-vs-code/images/select-linter.png?classes=shadow,border)
![Choose pylint](/01-introduction/02-requirements/05-vs-code/images/select-pylint.png?classes=shadow,border)
{{% /expand%}}