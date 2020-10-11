---
title: Requirements
weight: 3
---

{{% notice warning %}}
You'll need a few mandatory prerequisites for successfully participating in the course.
{{% /notice %}}

- A Linux, Mac OS, a Windows 10 Machine
- Python3.7
- Visual Studio Code
- The Python Extension for Visual Studio Code


#### Additional Instructions For Windows Users

- Note: Always select "Allow this app to make changes to your device" during the installation process.
- On the last page of the Python 3 installer, select "Disable Path Limit" before hitting close.
- In the start menu, right click on "Windows PowerShell". Select "Run as an administrator"
- In the PowerShell terminal window, that opens, type:

(`>` means prompt, don't type that in)

```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
```

Then, type `Y` for Yes.

{{% notice info %}}
Keep this window open for the following steps to create a virtual environment!
{{% /notice %}}

### Downloads

{{% button href="https://www.python.org/downloads/" icon="fas fa-download" %}}Download Python3{{% /button %}}
{{% button href="https://code.visualstudio.com/download" icon="fas fa-download" %}}Download Visual Studio Code{{% /button %}}
{{% button href="https://marketplace.visualstudio.com/items?itemName=ms-python.python" icon="fas fa-download" %}}Python Extension for Visual Studio Code{{% /button %}}

## Making sure you're ready

To make sure you have all the prerequisites properly installed:

### Checking for Python 3.7

#### For Windows

Using the same PowerShell window from earlier, type:

```powershell
> py -3.7
```

This should open a REPL window with a prompt.

{{% notice tip %}}
Press `Ctrl + Z` followed by Enter to exit this screen and go back to your prompt.
{{% /notice %}}

#### For Mac / Linux

Type the following on your terminal.
```bash
$ python3 --version
```

You should see
```bash
Python 3.7.2
```

{{% notice info %}}
If you don't see a Python version greater than 3.7, please follow the instructions for [installing Python3](https://www.python.org/downloads/) again.
{{% /notice %}}

### Creating a Virtual Environment and The Project Folder

A Virtual Environment in Python is a self-contained directory that contains a Python installation for a particular version of the language.

It's a very useful way to make sure that we're using the right Python version when we're working on a particular project.

Let's create a project directory and a Python 3.7 Virtual Environment.

#### For Windows

Using the same PowerShell terminal from earlier, type the following commands in one by one:

```powershell
> cd $home
> mkdir pyworkshop
> cd pyworkshop
> py -3 -m venv env
> env\scripts\activate
```

Your prompt should now look like this, but with your own username.

```powershell
(env) PS C:\Users\nina\pyworkshop>
```

{{% notice tip %}}
`env\scripts\activate` is how you *activate* your virtual environment in Windows. You'll want to do that each time you enter this Python project directory from a new shell.
{{% /notice %}}

#### For Mac / Linux

Open a terminal window. Type the following.

(Do not type the `$` character, that signifies a prompt.)

```bash
$ cd
$ mkdir pyworkshop
$ cd pyworkshop
$ python3.7 -m venv env
$ source env/bin/activate
```

{{% notice tip %}}
`source env/bin/activate` is how you *activate* your virtual environment on Mac or Linux. You'll want to do that each time you enter this Python project directory from a new shell.
{{% /notice %}}

Your prompt will look like this to indicate that the virtual environment is active.

```bash
(env) $
```

{{% notice info %}}
You are expected to work from this project folder for the duration of the class, with an activated virtual environment.
{{% /notice %}}

### Checking VS Code

Look for VS Code in your Applications, or type the following in your Mac/Linux *or* Powershell terminal.

```text
$ code --version
```

You should see something like:

```text
1.32.3
a3db5be9b5c6ba46bb7555ec5d60178ecc2eaae4
x64
```

{{% notice info %}}
If you don't see VS Code, please follow the instructions for [installing VS Code](https://code.visualstudio.com/download) again.
{{% /notice %}}

{{% notice note %}}
Note that after the course you can use the IDE of your choice to continue on your Python adventure.
{{% /notice %}}
