# Variables created inside a function are local.

def add():
    x = 10       #x and y are local variables and they can only be accessed inside the function
    y = 20
    print(x + y)

add()
# print(x)   #gives name error because x is not defined outside the function

print("\n")

# Variables created outside every function are global.

name = "Ayaan"

def greet():
    print(name)

greet()

print(name)

print("\n")

# Note-- Local variable shadows global variable with the same name.

name = "Ayaan"

def greet():
    name = "Rahul"
    print(name)

greet()

print(name)

# global keyword
# To modify a global variable inside a function, use global.

count = 0
def increment():
    global count
    count = count + 1

increment()

print(count)

print("\n")    #The function creates a new local variable instead of changing the global one if global keyword is not used.

score = 100
def update():
    global score
    score = 150

update()

print(score)

# Note
# we can only read a global variable inside a function without using the global keyword.
# if we need to modify a global variable inside a function, we must use the global keyword.