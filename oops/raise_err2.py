# val=input("enter number")
# if val.isdigit()==False:
#     raise Exception("only integer allowed")
# else:
#     print("valid input")

# #----------------------------------------------------------
#only alphabet and number allowed 

val=input("enter username")
if val.isalnum()==False:
    raise Exception("only interger and alphabet allowed")
else:
    print("valid input")