student={"name":"vishnu","age":23,"course":"django"}
print(student["name"])
print(student["age"])

print(student["course"])

#in
print("name" in student)

if "course" in student:
    print("present")
else:
    print("not present")

student["salary"]=25000   
print(student)

student["salary"]+=5000
print(student["salary"])




