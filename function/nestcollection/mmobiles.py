mobiles=[
    {"id":1,"name":"samsungs22","brand":"samsung","varients":[
        {"ram":"8gb","rom":"128gb","price":84000},
        {"ram":"8gb","rom":"256gb","price":100000},

    ]}, 
    {"id":1,"name":"samsungsa52","brand":"samsung","varients":[
        {"ram":"4gb","rom":"128gb","price":54000},
        {"ram":"8gb","rom":"256gb","price":650000},

    ]},
     {"id":1,"name":"one plus nord2","brand":"one plus","varients":[
        {"ram":"8gb","rom":"128gb","price":34000},
        {"ram":"8gb","rom":"256gb","price":450000},

    ]},
     {"id":1,"name":"miii1","brand":"redmi","varients":[
        {"ram":"8gb","rom":"128gb","price":24000},
        {"ram":"8gb","rom":"256gb","price":350000},

    ]},
]


# all_mobile_names=[mob.get("name")for mob in mobiles]          #all mobiles
# print(all_mobile_names)

# all_brands=[mob.get("brand") for mob in mobiles ]             #all brands
# print(set(all_brands))

# for mob in mobiles:
#     for v in mob.get("varients"):
#         if v.get("price") in range(20000,30001):
#             print(mob.get("name"))


# price_f=[mob.get("name") for mob in mobiles for v in mob.get("varients") if v.get("ram")=="4gb"]


# for mob in mobiles:
#     for v in mob.get("varients"):
#         if v.get("ram")=="4gb":
#             print(mob.get("name"))

# price_f=[mob.get("name") for mob in mobiles for v in mob.get("varients") if v.get("price") in range(20000,30001)]


# costly=max(mobiles,key=lambda mob:[v.get("price") for v in mob.get("varients")])
# print(costly)


price=[v.get("price") for mob in mobiles for v in mob.get("varients")]
print(price)

max_price=max(v.get("price") for mob in mobiles for v in mob.get("varients"))
print(max_price)