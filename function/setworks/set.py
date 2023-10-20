# set = {} # value koduthilangil dictionarybayit edkm   dictionaryim same ann
# duplication not allowed
# insertion order not correct
# metods= add,union,intersection,difference,pop,remove,discard,issubset,issuperset


# color_st={"red","blue","white",}

# color_st.add("yellow")                     #add

# print(color_st)



st1={"red","green","blue"}
st2={"red","purple","white","blue","green"}   

# union_st=st1.union(st2)                     #union
# print(union_st)


# intersection_st=st1.intersection(st2)
# print(intersection_st)                      #intersection


# lst1=[10,12,13,14,15]
# lst2=[11,13,14,15,16]

# st_lst1=set(lst1)
# st_lst2=set(lst2)

# # common_element=st_lst1.intersection(st_lst2)
# # print(common_element)


# diff_set=st_lst2.difference(st_lst1)         #difference
# print(diff_set)



# # st1.remove("red")                           #remove
# # print(st1)


# st1.pop()                                     #pop
# print(st1)


st1.discard("white")                            #discard
print(st1)

print(st1.issubset(st2))                        #issubset


print(st2.issuperset(st1))                      #issuperset