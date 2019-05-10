---
title: "Concept"
date: 2019-03-10T19:30:29-07:00
draft: false
weight: 1
---

Unit testing is a software testing method by which individual functions are tested in an automated fashion to determine if they are fit for use. Automated unit testing not only helps you discover and fix bugs quicker and easier than if you weren't testing, but by writing them alongside or even *before* your functions, they can help you write cleaner and more bug-free code from the very start.


### Types of Tests

There are several different kinds of automated tests that can be performed at different abstraction levels.

* Unit tests operate on the smallest testable unit of code, usually a function that performs a single action or operation.
* Integration tests check to see if different units or modules of code work together as a group.
* Functional tests operate on units of functionality, to make sure a specific function of the software is working, which may involve several units of software or whole systems working together.

For this class, we'll just be focusing on unit tests.


### Tests in the Real World™

How is this helpful in the real world? Many companies that invest in software development maintain a CI/CD (Continuous Integration or Continuous Deployment) pipeline. This usually involves extensive unit tests, integration tests, and maybe even functional tests, which are set up to run automatically after (and sometimes even *before*) code is committed. If the tests fail, deployment can be stopped and the developers get notified before broken code ever makes it to production servers. This can be complicated to set up properly, but saves an enormous amount of time in the long run, and helps to keep bugs from ever reaching your users.
