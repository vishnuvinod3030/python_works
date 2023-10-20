f_read=open("C:\\Users\\user\\Desktop\\my_pythonworks\\function\\fileoperation\\years.txt")

f_write=open("C:\\Users\\user\\Desktop\\my_pythonworks\\function\\fileoperation\\leap_years.txt","w")

for line in f_read:
    year=int(line.rstrip("\n"))
    if year%100==0 and year%400==0:
        f_write.write(str(year)+"\n")
    elif year%100!=0 and year%4==0:
        f_write.write(str(year)+"\n")