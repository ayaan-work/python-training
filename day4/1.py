# Object Oriented Programming is programming paradigm which classes and objects for building applications and it also uses real world modelling.

class Employee:
    name="Rohan"
    language="Py"      #class attribute
    salary=120000

obj1=Employee()
obj1.name="Ayaan"    #instance attribute takes preference over class atribute during assignment and retreival.
print(obj1.name,obj1.language,obj1.salary)