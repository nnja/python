---
title: "Mutability Cheat Sheet"
date: 2019-03-03T13:06:52-08:00
draft: false
weight: 65
---

### Mutability

Mutability, simply put: the contents of a mutable object can be changed, while the contents of an immutable object cannot be.

### Simple Types

All of the simple data types we covered first are **immutable**

| type                      	| use                     	| mutable? 	|
|---------------------------	|-------------------------	|----------	|
| `int`, `float`, `decimal` 	| store numbers           	| **no**   	|
| `str`                     	| store strings           	| **no**   	|
| `bool`                    	| store `True` or `False` 	| **no**   	|

### Container Types

For the mutability of the container types we covered in this chapter, check this helpful list:

| container type 	| use                                                                                                     	| mutable? 	|
|----------------	|---------------------------------------------------------------------------------------------------------	|----------	|
| `list`         	| ordered group of items, accessible by position                                                          	| **yes**  	|
| `set`          	| mutable unordered group consisting only of immutable items. useful for set operations (membership, intersection, difference, etc) 	| **yes**  	|
| `tuple`        	| contain ordered groups of items in an **immutable** collection                                          	| **no**   	|
| `dict`         	| contains key value pairs                                                                                	| **yes**  	|
