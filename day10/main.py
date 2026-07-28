def add(a,b):
    return a+b

def divide(a,b):
    if b==0:
        raise ValueError("Cannot divide by zero")
    return a/b


print(add(3,4))
# print(divide(10,0))
print(divide(20,2))