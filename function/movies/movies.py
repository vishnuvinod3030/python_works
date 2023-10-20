# from json import load
# f=open("C:\\Users\\user\\Desktop\\my_pythonworks\\function\\movies\\db.json")

# data=load(f)

# print(len(data))


from json import load
path="C:\\Users\\user\\Desktop\\my_pythonworks\\function\\movies\\db.json"

with open(path) as f:
    data=load(f)

all_names=[m.get("Title") for m in data ]
# print(all_names)

# print all director names
all_directors={m.get("Director") for m in data}
all_directors.discard("N/A")
print(all_directors)

filter_data=[m for m in data if m.get("imdbRating") !="N/A"]

top_movie=max(filter_data,key=lambda m:float(m.get("imdbRating")))

print(top_movie.get("Title"))



# print all movies with genre action
# /print all genre
# /movie released before 2014

all_genres=set()
for m in data:
    for g in m.get("Genre").split():
        all_genres.add(g.rstrip(","))
print(all_genres)