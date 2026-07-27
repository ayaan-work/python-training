# A module is simply a Python file (.py) containing functions, classes, variables, or executable code that can be reused in other Python programs.

# Instead of writing the same code repeatedly, you can place it in a module and import it whenever needed.

# Built in modules
# import math, import random, import os, import datetime, import json

#user defined modules
#created by us

#third party modules  (installed using pip)
# pip install requests, pip install numpy, pip install pandas


#. if name == "main"
# This prevents certain code from running when a module is imported.

# Example:
# #calculator.py

# def add(a, b):
#     return a + b

# if __name__ == "__main__":
#     print(add(2, 3))

# Running directly:
# 5

# Importing:
# import calculator
# Nothing prints.

# This is useful for:

# Testing
# Demo code
# Example usage


def add(a,b):
    return a+b