class Employee:
    language="javascript"
    salary=100000
    
    def __init__(self,language,salary):  ##constructor in python is made using __init__ keyword
        self.language=language 
        self.salary=salary
        
    def info(self):   
        print(f"your salary is {self.salary} and language is {self.language}")

    @staticmethod     
    def greet():
        print("good morning")


obj=Employee("Python",120000)   #instance attribute
obj.greet()
obj.info()


