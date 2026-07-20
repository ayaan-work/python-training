# Why Use @property?
# Suppose you have a class like this:
# class Student:
#     def __init__(self, marks):
#         self.marks = marks
# s = Student(95)
# print(s.marks)
# Output:
# 95
# The problem is that anyone can assign an invalid value:
# s.marks = -20
# Now the object contains incorrect data.
# Properties allow us to validate values before they are stored.
# The @property decorator converts a method into a read-only attribute.


class Employee:

    @property     #getter method
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter         #setter method
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]


obj=Employee()
obj.name="Ayaan Ahmad"     #Abstraction    
print(obj.name) 
print(obj.fname,obj.lname) 

print("\n")

class Student:

    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self._marks = value
        else:
            print("Invalid marks")


s = Student(90)

s.marks = 95
print(s.marks)

s.marks = 150

print("\n")
#classic getter setter with private variable (name mangling)

class Student:

    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, value):
        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("Invalid marks")


s = Student(90)

print(s.get_marks())

s.set_marks(95)
print(s.get_marks())

s.set_marks(150)

