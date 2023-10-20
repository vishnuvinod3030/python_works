
from re import *

varname=input("enter a variable name")
pattern="[a-zA-Z][a-zA-Z0-9]*"

matcher=fullmatch(pattern,varname)

if matcher ==None:
    print("invalid")
else:
    print("valid")
