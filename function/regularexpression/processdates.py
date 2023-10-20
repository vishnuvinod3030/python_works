from re import *
f=open("C:\\Users\\user\\Desktop\\my_pythonworks\\function\\regularexpression\\dates.txt")

# pattern="\d{4}[-]\d{2}[-]\d{2}"
# pattern="(20)([01][0-9]2[0-3])[-\]\d{2}[-\]\d{2}" # century year................
pattern="(20)([01][0-9]|2[0-3])[-\](0[1-9]|1[0-2])[-\]\d{2}" 
for line in f:
    date=line.rstrip("\n")
    matcher=fullmatch(pattern,date)
    if matcher !=None:
        print(date)