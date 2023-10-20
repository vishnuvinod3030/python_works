# "string"
# 'string'
# """string""" (more than one line)

# string ? sequence of charater

# name="Luminar Technolab"
# print(name.casefold())

# print(name.capitalize())

# print(name.count('a'))
# print(name.startswith("hu")) check the starting letter we assign

# print(name.endswith("lab"))

# print(name.isalpha())


name="hello,good,morning,all"

words=name.split(",") #line by line ayit print cheyum
for w in words:
    print(w)