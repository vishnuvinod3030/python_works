#student rollnum,course,total

class student:
    rol:int
    course:str
    total:int


    def __init__(self,rollnum,course,total):
        self.rol=rollnum
        self.course=course
        self.total=total
    def display(self):
        print(self.rol,self.course,self.total)

obj1=student(1000,"django",450)
obj1.display()
obj2=student(1001,"mernstack",480)
obj2.display()
obj3=student(1002,"django",490)
obj1.display()
