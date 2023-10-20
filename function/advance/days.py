lst=[i for i in range(1,8)]
print(lst)
#2-7 holiday  and 1,7 weekend
out=["Holiday" if i in (1,7) else "weekend" for i in lst ]
print(out)



lst=[2,3,-1,4,6,0,5,8]
#print all +ve number that are divisible by 3
output=[num for num in lst if(num>0) and (num%3==0)]
print(output)



#print(),input(),type(),len(),range(),sum(),max(),min(),sorted(),any()
