#Duck typing is a Python-specific way of using polymorphism. It does not require inheritance.

class Duck:
    def speak(self):
        print("Quack")


class Human:
    def speak(self):
        print("Hello")


def talk(obj):
    obj.speak()


d = Duck()
h = Human()

talk(d)
talk(h)


#the function talk(obj) doesn't check, it simply calls obj.speak() , If the object has a speak() method, everything works. 