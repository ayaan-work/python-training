class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s = Student("Ayaan", 95)

print(s)
#prints: <__main__.Student object at 0x000001D4F2B3A9A0>
#This isn't very helpful because Python prints the memory address of the object by default.

#__str__() → "How should I display this object to a user?"
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student(Name={self.name}, Marks={self.marks})"


s = Student("Ayaan", 95)

print(s)
#prints: Student(Name=Ayaan, Marks=95)
#Now the object is much easier to understand.

print("\n")

#__repr__() → "How should I represent this object for a developer or debugging?"
#it is meant for developers and debugging

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __repr__(self):
        return f"Student('{self.name}', {self.marks})"


s = Student("Ayaan", 95)

print(repr(s))

#Python falls back to __repr__() if __str__() is not defined.
