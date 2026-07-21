class Animal:
    def eat(self):
        print("Eating")


class Mammal(Animal):
    def walk(self):
        print("Walking")


class Dog(Mammal):
    def bark(self):
        print("Barking")


d = Dog()

d.eat()
d.walk()
d.bark()