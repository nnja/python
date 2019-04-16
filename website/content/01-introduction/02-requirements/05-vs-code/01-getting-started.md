---
title: "Getting Started"
draft: false
weight: 1
---

Visual Studio Code (commonly called VS Code) is a free, open source, lightweight cross platform code editor. A fresh installation is bare bones -- the power of VS Code comes via the extensions. There are useful extensions for every programming languages you can think of, but the choice of which ones to install and how to configure your editor is up to you.

## Installation

You should have installed the editor and the Python extension as part of the pre-requisites for the course. If you haven't, please do so now as we'll be using VS Code to edit our Python for the rest of the course.

 {{% button href="https://code.visualstudio.com/download" icon="fas fa-download" %}}Download Visual Studio Code{{% /button %}}

 {{% button href="https://marketplace.visualstudio.com/items?itemName=ms-python.python" icon="fas fa-download" %}}Python Extension for Visual Studio Code{{% /button %}}

## Advantages

You'll want to use a code editor for your Python projects as your projects grow in scope. It'll allow you to easily manage projects with multiple files and modules. The Python extension also offers a built-in REPL, so that we can quickly and easily test out snippets of code and instantly see the results.

Code editors also offer syntax highlighting, syntax checking, auto-completion, and more.

## Keyboard Bindings

If you prefer keyboard shortcuts from a different editor, such as sublime, vim, or emacs, you can install a [key-map extension](https://code.visualstudio.com/docs/getstarted/keybindings#_keymap-extensions) to remap your keybindings, preferably at the next break.

## Choices

We'll be using VS Code for this course so I can show you the ropes, but after class is over you're free to switch to any editor of your choice.

{{% notice info %}}
Note: For the rest of the course, instructions for Mac/Linux terminal and Windows PowerShell terminal should be the same.
{{% /notice %}}

## Opening Your First Project

#### Setting Up a Project Structure

Now that VS Code is downloaded and installed, it's time to open our project.

On Mac OS and Linux, follow these steps in you terminal application, or follow the steps manually in the program you use to manage files.

{{% notice tip %}}
Remember, you can copy all the commands by clicking on the<br/>
clipboard icon (<i class='fa fa-clipboard-list'></i>) located in the top right section of a code block.
{{% /notice %}}

```bash
# change to our home directory
$ cd

# enter the directory of the pyworkshop folder from the last step
$ cd pyworkshop
```

For Mac / Linux:

```bash
# activate the virtual environment
$ source env/bin/activate

# make a new empty python file called project.py
(env) $ touch project.py
```

For Windows:

```powershell
# activate the virtual environment
> env\scripts\activate

# make a new empty python file called project.py
(env)> fc > project.py
```

<!-- #### Opening a Project in VS Code

There are two ways to open projects. -->

#### Opening a Project in VS Code From The Command Line

First, navigate to your project directory and activate your virtual environment. If you followed the previous steps, you should already be in the right directory.

```bash
# Open VS Code using the current directory as a project.
(env) $ code .
```

This will open a project in the current directory. This is the last time we'll be using the terminal outside of VS Code for the duration of the course.

<!-- ##### Opening a Project in VS Code From The Application

The second way is to open the VS Code Application.

![Open The VS Code application](/01-introduction/02-requirements/05-vs-code/images/vs-code-icon.png?classes=shadow,border)

You should see a screen like this. If you don't, select **File -> New Window** from the menu.

![New Project Page](/01-introduction/02-requirements/05-vs-code/images/welcome-page.png?classes=shadow,border&width=50pc)

Select open folder, navigate to the `pyworkshop` folder in your home directory, select it, and click on open.

![Open Folder](/01-introduction/02-requirements/05-vs-code/images/open-folder.png?classes=shadow,border) -->


## Keyboard Shortcuts

To get started with VS Code, you only need to remember two keyboard shortcuts.

### #1 : Show Command Palette

Open the command palette with `Ctrl+Shift+P` on Windows and Linux, and `⌘⇧P` (command + shift + P) on Mac OS.

The command palette lets you search and run any of the commands available within VS Code. If you don't know how to do something, the command palette will usually point you in the right direction.

The command palette is how you'll navigate VS Code.

![Command Palette](/01-introduction/02-requirements/05-vs-code/images/command-palette.png?classes=shadow,border "The VS Code Command Palette")

### #2 : Quick Open, Go to File

Open Quick Open with `Ctrl+P` on Windows and Linux, and `⌘P`(command + P) on Mac OS.

Quick open is how you'll navigate your codebase and files.

**To dismiss either dialog, press the Escape key.**

{{% notice tip %}}
Write these two shortcuts down, because we'll be using them frequently for the rest of the course.
{{% /notice %}}