#!/bin/python3
"""
**kwargs allows you to pass keyworded variable length of arguments to a function.
You should use **kwargs if you want to handle named arguments in a function.
Here is an example to get you going with it:
"""


def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))


if __name__ == '__main__':
    greet_me(name='Mike', years_experience=5, location='Barcelona')
