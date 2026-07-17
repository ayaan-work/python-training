#A namedtuple creates a tuple whose elements can be accessed by name as well as by index.
#Since namedtuple is immutable, _replace() returns a new instance.

from collections import namedtuple
Student = namedtuple("Student", ["name", "age"])
s = Student("Ayaan", 22)
print(s)
print(s.name)
print(s.age)
print(s[0])
print(s[1])
print(s._asdict())

s2 = s._replace(age=23)
print(s2)