# Suppose the parent already has useful code.
# Instead of rewriting it, the child can call the parent's method using super().

class Animal:
    def sound(self):
        print("Animal sound")


class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog barks")


d = Dog()

d.sound()

# Without super(), only this would print: Dog barks

print("\n")

class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks


s = Student("Ayaan", 95)

print(s.name)
print(s.marks)
#super().__init__(name) initializes the name attribute in the parent class.

print("\n")

class Employee:

    def __init__(self, name):
        self.name = name

    def work(self):
        print(self.name, "is working")


class Developer(Employee):

    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

    def work(self):
        super().work()
        print("Writing", self.language, "code")


d = Developer("Ayaan", "Python")

d.work()