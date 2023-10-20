

f1=open("C://Users//user//Desktop//my_pythonworks//function//fileoperation//allstudents.txt","r")

f2=open("C://Users//user//Desktop//my_pythonworks//function//fileoperation//failed.txt","r")


all_students={line.rstrip("\n") for line in f1}

failed_students={line.rstrip("\n") for line in f2}

passed_students=all_students.difference(failed_students)
print(passed_students)