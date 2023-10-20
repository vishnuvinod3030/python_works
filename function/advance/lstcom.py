lst=[3,4,5,6,7,8]
#find cube
cubes=[num**3 for num in lst]#print cubes
print(cubes)


square=[num**2 for num in lst] #print square
print(square)


add_two=[num+2 for num in lst]#print add two
print(add_two)



odds=[num for num in lst if num %2!=0]
print(odds)

evens=[num for num in lst if num %2==0]
print(evens)