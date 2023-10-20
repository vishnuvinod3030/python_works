mobile={"code":"re100","name":"realme","processor":"snapdragon","price":22000}

print(mobile["name"])

# if "price" in mobile:
#     print(mobile["price"])
# else:
#     print("invalid")

# mobile["offer"]=2000
# mobile["price"]-=2000
# print(mobile)


mobile["offer"]="10%"
cur_price=mobile["price"]

discount=(cur_price/100)*10
mobile["price"]-=discount

print(discount)

print(mobile)