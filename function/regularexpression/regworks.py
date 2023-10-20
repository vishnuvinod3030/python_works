from re import *
text="ababcdabac"
#     01234567

pattern="ab"

matcher=finditer(pattern,text)
count=0
for m in matcher:
    print(m.start())
    print (m.group())
    count+=1

print("occurance of pattern=",count)