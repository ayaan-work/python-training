class Employee:
    language="Python"
    salary=1200000

    def info(self):   #self refers to the instance of the class. It is automatically passed with a function call from an object
        print(f"your salary is {self.salary} and language is {self.language}")


obj=Employee()
obj.info()
Employee.info(obj)  # internally the above function call changes to this

