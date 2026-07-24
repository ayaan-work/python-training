#Python decorators are a powerful and versatile tool that allow you to modify th behaviour of functions and methods.They are a way to extend the functionality of a function or method without modifying its source code.
#suppose we want some functionality to run every time when we call a function,  so we can make a decorator for it.

def greet(fx):
    def mfx(*args,**kwargs):
        print("Good Morning!")
        fx(*args,**kwargs)
        print("thank you for using this function")
    return mfx

@greet
def hello():
    print("Hello World")

@greet
def add(a,b):
    print(f"the sum is {a+b}")

hello()
print("\n")
add(2,3)

## Using functools.wraps
from functools import wraps

def decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        return func(*args, **kwargs)

    return wrapper

@decorator
def hello():
    """Print greeting"""
    print("Hello")

print(hello.__name__)
print(hello.__doc__)

#@wraps(func) copies important metadata like:
# Function name (__name__)
# Documentation (__doc__)
# Module (__module__)
# Other attributes

# It also helps debugging and documentation tools work correctly.

#A function can have multiple decorators.
def uppercase(func):

    @wraps(func)
    def wrapper():
        return func().upper()

    return wrapper


def exclaim(func):

    @wraps(func)
    def wrapper():
        return func() + "!"

    return wrapper  

@exclaim
@uppercase
def greet():
    return "hello"

print(greet())

#another example
def first(func):

    def wrapper():
        print("First Start")

        func()

        print("First End")

    return wrapper


def second(func):

    def wrapper():
        print("Second Start")

        func()

        print("Second End")

    return wrapper

@first
@second
def hello():
    print("Hello")

hello()