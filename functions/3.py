# *args allows a function to accept any number of positional arguments.

def add(*args):
    print(args)

add(1)
add(1, 2)
add(1, 2, 3)     #this will be treated as a tuple inside the function
add(1, 2, 3, 4)

print("\n")

def add(*args):
    total=0
    for num in args:
        total+=num
    return total

ans=add(1, 2, 3, 4, 5)
print(ans)    

print("\n")

# **kwargs allows a function to accept any number of keyword arguments.
# kwargs is a dictionary./

def info(**kwargs):
    print(kwargs)

info(name="Ayaan", age=22)

print("\n")

def info(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

info(name="Ayaan", age=22, city="Delhi")