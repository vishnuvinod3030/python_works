num1=25
num2=13
num3=18

if(num1 > num2)and(num1 >num3):
    if(num2>num3):
        print("num2 is secnd larger")
    else:
        print("num3 secnd larg.")
elif(num2 >num1)and(num2 >num3):
    if(num1>num3):
        print("num1 is secnd larger")
    else:
        print("num3 is secnd larg.")
elif(num3 >num1)and(num3 >num2):
    if(num1>num2):
        print("num1 is scnd larger")
    else:
        print("num2 is scnd larger")