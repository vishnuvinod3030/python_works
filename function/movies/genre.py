from json import load
path="C:\\Users\\user\\Desktop\\my_pythonworks\\function\\movies\\db.json"

with open(path) as f:
    data=load(f)


# print all movies with genre action
# /print all genre
# /movie released before 2014



all_genres=set()
for m in data:
    for g in m.get("Genre").split():        #print all genre
        all_genres.add(g.rstrip(","))
print(all_genres)


for mv in data:
    if mv.get("Genre").count("Action")>0:   #genre with action
        print(mv.get("Title"))


for mv in data:
    r_date=mv.get("Released")
    year=r_date.split(" ")[-1]
    
    if year.isdigit():
        if int(year)>2014:
            print(mv.get("Title"),mv.get("Released"))