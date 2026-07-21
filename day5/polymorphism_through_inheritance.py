# Polymorphism Through Inheritance

# This is where method overriding comes in.
class Animal:
    def sound(self):
        print("Some sound")


class Dog(Animal):
    def sound(self):
        print("Bark")


class Cat(Animal):
    def sound(self):
        print("Meow")


animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()


#The loop doesn't care whether it's a Dog or a Cat. It simply calls sound().
