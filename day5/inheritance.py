#inheritance is a technique in which one class uses the variables and properties of other class, it enables code reusability
class Employee:
    company="ITC"

    def show(self):
        print(f"this is the base class")

class Programmer(Employee):
    company="ITC Infotech"

    def skill(self,name,language):
        print(f"{name} is very good at {language} and is currently working in {self.company}")

a=Employee()
print(a.company)
a.show()

b=Programmer() 
print(b.company)
b.show()
b.skill("Ayaan","Python")





