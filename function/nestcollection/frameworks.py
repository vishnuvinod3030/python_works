frameworks=[
    {"id":1,"name":"django","rating":5,"language":"python"},
    {"id":2,"name":"angular","rating":4,"language":"typescript"},
    {"id":3,"name":"react","rating":5,"language":"javascript"},
    {"id":4,"name":"spring","rating":3,"language":"java"},
    {"id":5,"name":"asp.net","rating":2,"language":"c#"},
    {"id":6,"name":"flask","rating":3,"language":"python"},]


# for fw in frameworks:
#     print(fw.get("name"))



# for fw in frameworks:
#     print(fw.get("language"))


# fw_names=[fw.get("name") for fw in frameworks ]
# print(fw_names)                                                #list ayit print cheyan (one linil)

# all_rating=[fw.get("rating") for fw in frameworks]
# print(all_rating)

python_fw=[fw.get("name") for fw in frameworks if fw.get("language")=="python"]
print(python_fw)
                                                                                        # python frame works name 
rating_filter=[fw.get("name") for fw in frameworks if fw.get("rating")==5]
print(rating_filter)
#python frame works name 


#id 1 to 3

# id_filter=[fw.get("name") for fw in frameworks if fw.get("id") in range(1,4)]
# print(id_filter)

# lowest rating 
lw_rating=min(frameworks,key= lambda fw:fw.get("rating"))
print(lw_rating)

top_rating=max(frameworks,key=lambda fw:fw.get("rating"))
print(top_rating)

srt=sorted(frameworks,key=lambda fw:fw.get("rating"))
print(srt)

