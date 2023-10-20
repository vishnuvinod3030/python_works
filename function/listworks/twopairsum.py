# sum=int(input("enter sum>"))
# arr=[2,4,5,6,8]

# # sr_arr=sorted(arr)
# arr.sort()
# low=0
# upp=len(arr)-1

# while(low<upp):
#     cur_sum=arr[low]+arr[upp]                  print only one pair

#     if cur_sum==sum:
#         print("pairs",arr[low],arr[upp])
#         break
#     elif cur_sum<sum:
#         low+=1
#     elif cur_sum>sum:
#         upp-=1





sum=int(input("enter sum>"))
arr=[2,4,5,6,8]

# sr_arr=sorted(arr)
arr.sort()
low=0
upp=len(arr)-1

while(low<upp):
    cur_sum=arr[low]+arr[upp]              #print all existing pair                                   
    if cur_sum==sum:
        print("pairs",arr[low],arr[upp])
        low+=1
        upp-=1
    elif cur_sum<sum:
        low+=1
    elif cur_sum>sum:
        upp-=1