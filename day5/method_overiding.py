# Sometimes the child wants to change the parent's behavior.

# This is called method overriding.

class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


d = Dog()

d.sound()

# Python always checks:
# 1)Child class
# 2)Parent class