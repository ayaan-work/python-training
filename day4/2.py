class Student:

    school = "ABC School"

    def __init__(self, name):
        self.name = name

    # Instance Method
    def display(self):
        print(self.name)

    # Class Method
    @classmethod
    def display_school(cls):
        print(cls.school)

    # Static Method
    @staticmethod
    def greet():
        print("Welcome!")

s1 = Student("Ayaan")

s1.display()

Student.display_school()

Student.greet()

print("\n")

#alternative constructor

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split("-")
        return cls(name, int(age))

s1 = Student.from_string("Ayaan-22")

print(s1.name)
print(s1.age)