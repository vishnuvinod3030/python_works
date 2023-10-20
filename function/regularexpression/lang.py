#starting with an alphabet k,l,m,n
# second that must bea digit and divisible by 3
# followed by any number of alphabets and digits


from re import *
var_name=input("enter variabe name:>")
pattern="[k-n][369][a-zA-Z0-9]*"

matcher=fullmatch(pattern,var_name)
print("invalid" if matcher == None else "valid")