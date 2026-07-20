class Employee:
    language="Python"
    salary=1200000

    def info(self):   
        print(f"your salary is {self.salary} and language is {self.language}")

    @staticmethod      #here we can omit self as the function doesnt need values from object, this is called static method
    def greet():
        print("good morning")


obj=Employee()
obj.greet()
obj.info()


