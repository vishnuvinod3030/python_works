#dictionary method###############
# GET("KEYS"),POP("KEY"),ITEM(),VALUES(),KEYS()
animals={"a":"apple","b":"banana","c":"cat","d":"dog","e":"elephnat"}

# print all keys################################
# keys()#####################################

# for k in animals.keys():
#     print(k)

# #values()=>return all values from dictionary##########

# for v in animals.values():
#     print(v)

print(animals.get("w"))


#items()=>return key , values

# for k,v in animals.items():
#     print(k,v)


animals.pop("a")
print(animals)