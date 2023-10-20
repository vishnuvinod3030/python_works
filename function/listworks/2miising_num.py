lst=[1,2,3,4,5,6]

limit=len(lst)-1

i=0
while(i<limit):
    j=i+1

    diff=lst[j]-lst[i]
    if(diff==1):
        i+=1
    else:
        print(lst[i]+1,"is missing")
        break