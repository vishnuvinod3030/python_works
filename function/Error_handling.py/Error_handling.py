n1=int(input("enter a num1"))
n2=int(input("enter a num2"))
lst=[10,20,56]

loc=int(input("enter index position to fect object"))#10

try:
    print(lst[loc]) #index out of range
except Exception as e:
    print(e.args)

try:
    res=n1/n2  # n2 evide zero vanna error form cheyum ,so try,except use cheyum
    print(f"result={res}")

except Exception as e:
    print("exception occured")


print("database commited")
print("file transaction")

#try = doubtful code
#except= exception code
#finally block - mandatory to print
#raise -keyword to throw custom error