# bmi

weightin_kg=66
heightin_cm=170
heightin_meter=heightin_cm/100
bmi=weightin_kg/(heightin_meter**2)
print(bmi)

if(bmi <20):
    print("under weight")
elif(bmi >=20 and bmi <25):
    print("normal weight")
elif(bmi>= 25 and bmi <30):
    print("over weight")
else:
    print("obesity")