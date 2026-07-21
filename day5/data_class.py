# @dataclass is one of Python's most useful features (introduced in Python 3.7). It automatically generates common methods like __init__(), __repr__(), and __eq__() for classes that mainly store data.
#"You only tell me what data your class has, and I'll write the boilerplate code for you."

#without dataclass
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __repr__(self):
        return f"Student(name='{self.name}', marks={self.marks})"


s = Student("Ayaan", 95)

print(s)

print("\n")

#with dataclass
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    marks: int

s = Student("Ayaan", 95)

print(s)
#Pyhton automatically generates __init__(),__repr__(),__eq__()

print("\n")

#Field Defaults

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    marks: int = 0

s = Student("Ayaan")

print(s)   #Student(name='Ayaan', marks=0) If you don't pass marks, it defaults to 0.

print("\n")

#field()
# @dataclass
# class Student:
#     subjects: list = []
#All objects would share the same list.

from dataclasses import dataclass, field

@dataclass
class Student:
    name: str
    subjects: list = field(default_factory=list)    #Instead of reusing one list, Python calls list() each time a new object is created.

s1 = Student("Ayaan")
s2 = Student("Ali")

s1.subjects.append("Python")

print(s1.subjects)               #['Python']
print(s2.subjects)               #[]

print("\n")

#frozen=True
#This makes the dataclass immutable.

from dataclasses import dataclass

@dataclass(frozen=True)
class Student:
    name: str
    marks: int

s = Student("Ayaan", 95)

s.marks = 100
#if we print(s)
# FrozenInstanceError:
# cannot assign to field 'marks'

# Use it for data that should never change, such as:
# Employee ID
# Date of birth
# GPS coordinates
# Configuration values

