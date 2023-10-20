lst=[3,5,4] #9,7,8

# 12-3=9
# 12-5=7
# 12-4=8

total=sum(lst)

for i in range(0,len(lst)):
    res=total-lst[i]
    print(res)