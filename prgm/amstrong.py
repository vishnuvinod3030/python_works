num=input("enter a number")
digit_count=len(num)
num=int(num)
original=num

sum=0
while(num!=0):
    last_digit=num %10
    power=last_digit**digit_count
    sum=sum+power
    num=num//10
print("amstrong Number"if sum==original else "Not Amstrong")
