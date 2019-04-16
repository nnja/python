---
title: "Running Code"
date: 2019-02-10T18:14:45-08:00
draft: false
weight: 5
---

VS Code provides a built in terminal that allows us to easily run our programs. We'll mostly be working with Python program files at the end of Day 1, and for most of Day 2.

### Creating Python Files with the `*.py` extension

You know a file is a Python program when it ends with a `.py` extension.

#### Creating New Python Files

To create a new file in VS Code, hit `Ctrl+N` on Windows and Linux, and `⌘N` (command + N) on Mac OS.

This will open a new file. Next, save the file with a `.py` extension.

{{% notice info %}}
Create a new simple Python program in a file called `hello.py` in your `pyworkshop` directory with the following contents:
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