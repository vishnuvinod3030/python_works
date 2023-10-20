# #set_employee
# class Employee:
#     id:int
#     name:str
#     dept:str
#     salary:int

#     def set_employee(self,id,name,dept,salary):
#         #instance variable(attribute) self. frntil vanne
#          #intializing 
#         self.id=id
#         self.name=name
#         self.dept=dept
#         self.salary=salary

#     def display(self):
#         print((self.id,self.name,self.dept,self.salary))


# #reference_name=classname()
# emp1=Employee()
# emp1.set_employee(1000,"vinay","manager",120000)
# emp1.display()
# emp2=Employee()
# emp2.set_employee(1001,"helta","manager",150000)
# emp2.display()
# emp3=Employee()
# emp3.set_employee(1002,"hari","manager",170000)
# emp3.display()




# using constructor

#set_employee
class Employee:
    id:int
    name:str
    dept:str
    salary:int
    company_name:str="UST"

    def __init__(self,id,name,dept,salary):
        #instance variable(attribute) self. frntil vanne
         #intializing 
        self.id=id
        self.name=name
        self.dept=dept
        self.salary=salary

    def display(self):
        print(self.id,self.name,self.dept,self.salary)

    def __Str__(self):
        return self.name


#reference_name=classname()
emp1=Employee(1000,"vinay","manager",120000)
emp1.display()
emp2=Employee(1000,"vinay","manager",150000)
emp2.display()
emp3=Employee(1002,"hari","manager",170000)
emp3.display()