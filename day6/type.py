#type in python

n : int = 5    #explicitly write the type of the variable for convenience so that no mistakes are made
day : str = "Monday"
salary: float = 45000.50
is_employee: bool = True

print(n)
print(day)

#declaring a function with types
def sum(a: int,b: int)-> int:
    return a+b

print(sum(3,6))
