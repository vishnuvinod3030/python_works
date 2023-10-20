from re import *#vehicle number
# veh_num=input("enter vehicle number")
# pattern="(KL)[-\s]?\d{2}[-\s]?[A-Z]{1,2}[-\s]?\d{4}"

# matcher=fullmatch(pattern,veh_num)
# print("invalid" if matcher == None else "valid")




#yyyy-mm-dd
# .................................


data=input("enter date")
pattern="\d{4}[-]\d{2}[-]\d{2}"

matcher=fullmatch(pattern,data)
print("invalid" if matcher == None else "valid")