lst=[10,11,12,13,14,15]

num=3
for i in range(0,len(lst)):              #break adicha last else work avilla
               
    if num==lst[i]:
        print("element found")
        break
else:
    print("element not found")
               