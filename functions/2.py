#positional arguments
def greet(name, age):
    print(f"Name: {name}")   #here the position matters
    print(f"Age: {age}")

greet("Ayaan", 22)
print("\n")

#keyword arguments
def greet(name, age):
    print(name)         #here the position does not matter
    print(age)

greet(age=22, name="Ayaan")
print("\n")

#default arguments
def greet(name="Guest"):
    print("Hello", name)     #the default argument will run if not explicitly passed 

greet()
greet("Ayaan")