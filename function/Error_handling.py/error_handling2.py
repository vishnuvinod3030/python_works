n1=int(input("enter a num1"))
n2=int(input("enter a num2"))


try:
    res=n1/n2  # n2 evide zero vanna error form cheyum ,so try,except use cheyum
    print(f"result={res}")

except Exception as e:
    print(e.args)

finally:
    print("database commited")
    print("file transaction")

#finally block - mandatory to print




