---
title: "How To Run Them"
date: 2019-02-10T18:17:06-08:00
draft: false
weight: 10
---

### Creating Python Files with the `*.py` extension

You know a file is a Python program when it ends with a `.py` extension.

#### Naming Tips

{{% notice tip %}}
Just like with formatting, Python's [PEP8 guidelines](https://www.python.org/dev/peps/pep-0008/#package-and-module-names) give us a few helpful tips about how to name our Python program files.
{{% /notice %}}

ℹ️ In Python:

1. Filenames should be ***all lowercase**
1. Words should be separated with **underscores `_`**
1. Filenames should be **short**

✅ Some good example filenames:

- `apis.py`
- `exceptions.py`
- `personal_blog.py`

⛔️ Some bad example filenames:

- `MYFILE.PY`
- `CamelCaseFile.py`
- `really_long_over_descriptive_project_file_name.py`


#### What are `*.pyc` files?

{{% notice note %}}
For optimization and other reasons, Python code can be compiled to intermediary `.pyc` files. The good news is you don't have to worry about them. The bad news is, very occasionally stale versions of these compiled files can cause problems. To safely delete them from the current project directory, run `find . -name "*.pyc" -delete` (on linux or macOS).
{{% /notice %}}

#### `git` tip: use a `.gitignore` for Python

If you use `git` for source control, you'll want to make sure that these compiled `*.pyc` files are ignored, and not added to your repository.

The best way to do this is to [add the standard `.gitignore` file for Python](https://github.com/github/gitignore/blob/master/Python.gitignore) to your project.


### Running Python Files From VS Code

Running Python files from VS Code is really quick and easy.

#### Creating New Python Files

To create a new file in VS Code, hit `Ctrl+N` on Windows and Linux, and `⌘N` (command + N) on Mac OS.

This will open a new file. Next, save the file with a `.py` extension.

{{% notice info %}}
Create a new simple Python program in a file called `hello.py` in our `pyworkshop` direc tory with the following contents:
{{% /notice %}}

```python
# in file: hello.py
greetings = ["Hello", "Bonjour", "Hola"]

for greeting in greetings:
    print(f"{greeting}, World!")
```

#### Opening The VS Code Terminal Window

Next, you'll need to open your terminal if you don't have it open already. The quick keyboard shortcut to do that is <code>Ctrl - &#96;</code>

{{% notice note %}}
If you already had your Python REPL open, you'll need to select a terminal with a shell in it (generally, the one labeled with `1:`).
{{% /notice %}}

![](/02-introduction-to-python/175-running-code/images/terminal-drop-down.png)
![](/02-introduction-to-python/175-running-code/images/terminal-drop-down-select.png)

#### Running The File

Once you've opened your `hello.py` file and selected your new terminal window, open the VS Code command palette.

{{% notice note %}}
Open the command palette with `Ctrl+Shift+P` on Windows and Linux, and `⌘⇧P` (command + shift + P) on Mac OS.
{{% /notice %}}

Select Python: Run Python File in Terminal

![](/02-introduction-to-python/175-running-code/images/vs-code-run-file-command-palette.png)

You should see:

```bash
Hello, World!
Bonjour, World!
Hola, World!
```

How easy was that? 🎉

### Running Python Files From a Non-VS Code Terminal

If you want to run a Python file without using the command palette, just open your terminal of choice, `cd` into the directory with your code, and type in the command `python` followed by a space, and the name of your Python program.

```bash
(env) $ python hello.py
Hello, World!
Bonjour, World!
Hola, World!
```

This also works in the VS Code terminal.