from json import load
path="C:\\Users\\user\\Desktop\\my_pythonworks\\function\\products\\item.json"
with open(path,encoding="UTF-8") as f:
    data=load(f)

#print total num of data

print(len(data))


# QUE PRINT all categories

# q2 print all electronic product name

# q3 top rated prtoduct

# q4 product got most number of rating

# q5 product having categories women's clothing 

# q6 jwellery product with rating>3


# q1

# all_categories={p.get("category") for p in data}
# print(all_categories)

# q2

# e_category=[p.get("title")for  p in data if p.get("category") =="electronics"]
# print(e_category)


# q3


# top_rating=max(data,key=lambda p:float(p.get("rating").get("rate")))
# print(top_rating.get("title"))


# q4

# m_reviewed_product=max(data,key=lambda p:p.get('rating').get("count"))
# print(m_reviewed_product.get("title"))


# q5


# for p in data:
#     if p.get("category")=="women's clothing" and p.get("price")>20 and p.get("price")<=30:
#         print(p.get("title"))


# q6
# for p in data:
#     if p.get("category")=="jewelery" and p.get("rating").get("rate")>3:
#         print(p.get("title"))


# q7

# srt_items=sorted(data,reverse=True,key=lambda p:p.get("price"))
# print(srt_items)


# srt_items=sorted(data,reverse=True,key=lambda p:p.get("price"))
# for p in srt_items:                 #titile sort cheyan
#     print(p.get("title"))



# q8

wc={}
for p in data:
    category=p.get("category")
    if category not in wc:
        wc[category]=1
    else:
        wc[category]+=1
print(wc)


val_key=[(v,k) for k,v in wc.items()]
print(sorted(val_key))
print(max(val_key))