# These annotations help in making the code self-documenting and allow developers to understand the data structures used at a glance
from typing import List,Tuple,Dict,Union,Optional,Any,Callable,TypedDict

numbers : List[int] = [1,2,3,4,5]

person : Tuple[str,int] = ("Ayaan", 23)

scores : Dict[str,int] = {"Rohan": 90, "Ritik": 93}

identifier : Union[str,int] = "Id123"
print(identifier)

identifier=123

def display(value: int | str):  #union shortcut
    print(value)  

display(10)
display("Hello")

print(numbers)
print(person)
print(scores)
print(identifier)

print("\n")

#Use Optional when a parameter isn't required.
def greet(name: Optional[str]) -> None:
    if name is None:
        print("Hello Guest")
    else:
        print(f"Hello {name}")

greet("Ayaan")
greet(None)

print("\n")

#Any--Means accept literally anything.
def print_value(value: Any):
    print(value)

print_value(10)
print_value("Python")
print_value([1, 2, 3])
print_value({"a": 1})

print("\n")

#Callable represents a function    Callable[[parameter_types], return_type]
#Think of Callable as "a variable that stores a function."

def add(a: int, b: int) -> int:
    return a + b

def operate(func: Callable[[int, int], int], x: int, y: int):
    return func(x, y)

print(operate(add, 5, 3))

print("\n")

#Used when a dictionary should have a fixed structure.
#Dictionary with predefined keys and value types (API responses, configuration objects)
class Student(TypedDict):
    name: str
    age: int

student: Student = {
    "name": "Ayaan",
    "age": 22
}

print(student["name"])