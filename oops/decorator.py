class employee:
    def __init__(self,name,salary,dept):
        self.name=name
        self.salary=salary
        self.dept=dept

    @property           # @property method classine functiono allengil property akum
    def get_name(self):
        return self.name
    
    @property
    def get_salary(self):
        return self.salary
    
emp=employee("hari",55000,"QA")

print(emp.get_name)  #  evide get_name kazhinj () ollatha edanda avisham illa
print(emp.get_salary)
print(emp.__class__)  #emp class ethann ariyaan
