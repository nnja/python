Local setup instructions:

1. Install Hugo version v0.54.0 for the site to render properly
1. clone hugo learn theme from https://github.com/matcornic/hugo-theme-learn, update `themesdir` in config.toml
1. `cd python` then, `hugo server -D` to run local server

Note: the file and folder names don't contribute to order, and may not always be accurate. Sorted by chapter and individual page weight.

If you move things around or delete chapters, you may have to restart the server for the chapters to appear correctly.

How to use the theme: https://learn.netlify.com/en/cont/
More about theme shortcodes: https://learn.netlify.com/en/shortcodes/

use `git lfs` for tracking binary types.

```bash
$ git lfs track "*.psd"
git add .gitattributes

36% off
Learn to code by doing. Try hands-on Python with Programiz PRO. Claim Discount Now
Programiz
Courses
Tutorials
Examples

Search tutorials & examples
Try
Programiz PRO

Learn Python Interactively
Python Examples
Check if a Number is Positive, Negative or 0
Check if a Number is Odd or Even
Check Leap Year
Find the Largest Among Three Numbers
Check Prime Number
Print all Prime Numbers in an Interval
Find the Factorial of a Number
Display the multiplication Table
Python Tutorials
Python break and continue
Python while Loop
Python for Loop
Python if...else Statement
Python Operators
Python Functions
Python Program to Check Prime Number
To understand this example, you should have the knowledge of the following Python programming topics:

Python if...else Statement
Python for Loop
Python break and continue
Learn Python with Challenges
Solve challenges and become a Python expert.


A positive integer greater than 1 which has no other factors except 1 and the number itself is called a prime number. 2, 3, 5, 7 etc. are prime numbers as they do not have any other factors. But 6 is not prime (it is composite) since, 2 x 3 = 6.

Example 1: Using a flag variable
# Program to check if a number is prime or not

num = 29

# To take input from the user
#num = int(input("Enter a number: "))

# define a flag variable
flag = False

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

    # check if flag is True
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")
Run Code
Output

29 is a prime number
In this program, we have checked if num is prime or not. Numbers less than or equal to 1 are not prime numbers. Hence, we only proceed if the num is greater than 1.

We check if num is exactly divisible by any number from 2 to num - 1. If we find a factor in that range, the number is not prime, so we set flag to True and break out of the loop.

Outside the loop, we check if flag is True or False.

If it is True, num is not a prime number.
If it is False, num is a prime number.
Note: We can improve our program by decreasing the range of numbers where we look for factors.

In the above program, our search range is from 2 to num - 1.

We could have used the range, range(2,num//2) or range(2,math.floor(math.sqrt(num)+1)). The latter range is based on the fact that a composite number must have a factor less than or equal to the square root of that number. Otherwise, the number is prime.

You can change the value of variable num in the above source code to check whether a number is prime or not for other integers.

In Python, we can also use the for...else statement to do this task without using an additional flag variable.

Example 2: Using a for...else statement
num = 407

# To take input from the user
#num = int(input("Enter a number: "))

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")
Run Code
Output

407 is not a prime number
11 times 37 is 407
Here, we have used a for..else statement to check if num is prime.

It works on the logic that the else clause of the for loop runs if and only if we don't break out the for loop. That condition is met only when no factors are found, which means that the given number is prime.

So, in the else clause, we print that the number is prime.

Share on:
Did you find this article helpful?
Related Examples
Python Example

Print all Prime Numbers in an Interval

Python Example

Find the Factorial of a Number

Python Example

Find the Factors of a Number

Python Tutorial

Python break and continue


Join our newsletter for the latest updates.
Enter Email Address
Join


Tutorials
Python 3 Tutorial
JavaScript Tutorial
SQL Tutorial
HTML Tutorial
R Tutorial
C Tutorial
C++ Tutorial
Java Tutorial
Rust Tutorial
Go Tutorial
Kotlin Tutorial
Swift Tutorial
C# Tutorial
DSA Tutorial
Examples
Python Examples
JavaScript Examples
C Examples
Java Examples
Kotlin Examples
C++ Examples
Company
About
Advertising
Privacy Policy
Terms & Conditions
Contact
Blog
Careers
Youtube
Apps
Learn Python
Learn C Programming
Learn Java
© Parewa Labs Pvt. Ltd. All rights reserved.

   
  <h1><a href="https://github.com/TheAlgorithms/">The Algorithms</a> - Python</h1>
<!-- Labels: -->
  <!-- First row: -->
  <a href="https://gitpod.io/#https://github.com/TheAlgorithms/Python">
    <img src="https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod&style=flat-square" height="20" alt="Gitpod Ready-to-Code">
  </a>
  <a href="https://github.com/TheAlgorithms/Python/blob/master/CONTRIBUTING.md">
    <img src="https://img.shields.io/static/v1.svg?label=Contributions&message=Welcome&color=0059b3&style=flat-square" height="20" alt="Contributions Welcome">
  </a>
  <img src="https://img.shields.io/github/repo-size/TheAlgorithms/Python.svg?label=Repo%20size&style=flat-square" height="20">
  <a href="https://discord.gg/c7MnfGFGa6">
    <img src="https://img.shields.io/discord/808045925556682782.svg?logo=discord&colorB=7289DA&style=flat-square" height="20" alt="Discord chat">
  </a>
  <a href="https://gitter.im/TheAlgorithms">
    <img src="https://img.shields.io/badge/Chat-Gitter-ff69b4.svg?label=Chat&logo=gitter&style=flat-square" height="20" alt="Gitter chat">
  </a>
  <!-- Second row: -->
  <br>
  <a href="https://github.com/TheAlgorithms/Python/actions">
    <img src="https://img.shields.io/github/workflow/status/TheAlgorithms/Python/build?label=CI&logo=github&style=flat-square" height="20" alt="GitHub Workflow Status">
  </a>
  <a href="https://lgtm.com/projects/g/TheAlgorithms/Python/alerts">
    <img src="https://img.shields.io/lgtm/alerts/github/TheAlgorithms/Python.svg?label=LGTM&logo=LGTM&style=flat-square" height="20" alt="LGTM">
  </a>
  <a href="https://github.com/pre-commit/pre-commit">
    <img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=flat-square" height="20" alt="pre-commit">
  </a>
  <a href="https://github.com/psf/black">
    <img src="https://img.shields.io/static/v1?label=code%20style&message=black&color=black&style=flat-square" height="20" alt="code style: black">
  </a>
<!-- Short description: -->
  <h3>All algorithms implemented in Python - for education</h3>
</div>
Python program to find the
# quotient and remainder
 
def find(n, m):
     
    # for quotient
    q = n//m
    print("Quotient: ", q)
     
    # for remainder
    r = n%m
    print("Remainder", r)
     
# Driver Code
find(10, 3)
find(99, 5)
Implementations are for learning purposes only. As they may be less efficient than the implementations in the Python standard library, use them at your discretion.

## Getting Started

Read through our [Contribution Guidelines](CONTRIBUTING.md) before you contribute.

## Community Channels

We're on [Discord](https://discord.gg/c7MnfGFGa6) and [Gitter](https://gitter.im/TheAlgorithms)! Community channels are great for you to ask questions and get help. Please join us!

## List of Algorithms

See our [directory](DIRECTORY.md) for easier navigation and better overview of the project.
```

Currently tracked types:
 - .png
 - .jpg
 - .jpeg
 - .pdf
 - .mp4
 - .gif
