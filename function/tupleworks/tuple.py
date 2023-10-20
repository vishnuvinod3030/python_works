#(,) define
# insertion order is preserved in tuple
#duplication is allowed in tuple
# tuple method = count,index

tp=(10,20,30,30,40,50)
print(tp)
# tp[2]=200 #updation is not allowed in tuple


num_count=tp.count(30)  # count
print(num_count)

print(tp.index(30))    # index