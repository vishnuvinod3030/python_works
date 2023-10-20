from json import load

# f=open("C:\\Users\\user\\Desktop\\my_pythonworks\\function\\process_json\\student.json","r")

# data=load(f)
# print(len(data))


path="C:\\Users\\user\\Desktop\\my_pythonworks\\function\\process_json\\student.json"
with open(path) as f:
    data=load(f)
print(len(data))



