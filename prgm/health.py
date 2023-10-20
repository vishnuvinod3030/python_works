gender="male"
tummy_size=75
buttock_size=75
value=tummy_size/buttock_size
print(f"{value}")

if(gender=="male"):
    if(value <=0.95):
        print("health risk = low")
    elif(value>=0.95 and value <1):
        print("health risk = moderate")
    else:
        print("health risk = high")
elif(gender=="female"):
    if(value <=0.80):
        print("health risk = low")
    elif(value>=0.81 and value <0.85):
        print("health risk = moderate")
    else:
        print("health risk = high")
