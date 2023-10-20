# swapping

num1=10
num2=20
print(f"values b4 swapping num1={num1},num2={num2}") #10,20
# temp=num1
# num1=num2
# num2=temp
# print(f"values after swapping num1={num1},num2={num2}") #10,20

# logic2

# num1=num1+num2  #num1=10+20=30
# num2=num1-num2  #num2=30-20=10
# num1=num1-num2  #num1=30-10=20

# logic3
(num1,num2)=(num2,num1)
print(f"values after swapping num1={num1}, num2={num2}")#10,20