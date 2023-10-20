from re import *
data=input("enter gmail")#jhonda@live.com
pattern="[a-z0-9_.]+@[a-z]{2,}.com"

matcher=fullmatch(pattern,data)
print("invalid" if matcher == None else "valid")