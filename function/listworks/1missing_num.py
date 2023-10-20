lst=[1,2,3,4,6]

max_num=max(lst)

total_sum=max_num*(max_num+1)/2

cur_sum=sum(lst)                          #only for one missing num

diff=total_sum-cur_sum

if(diff==0):
    print(max+1,"is least positive missing number")
else:
    print(diff,"missing number")