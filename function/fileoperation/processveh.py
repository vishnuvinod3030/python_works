f_read=open("C:\\Users\\user\\Desktop\\my_pythonworks\\function\\fileoperation\\vehiclenum.txt")

f_write=open("C:\\Users\\user\\Desktop\\my_pythonworks\\function\\fileoperation\\keralanum.txt","w")


for line in f_read:
    reg_number=line.rstrip("\n")

    if reg_number.startswith("kl"):
        f_write.write(reg_number+"\n")