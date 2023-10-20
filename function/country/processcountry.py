from json import load

path="C:\\Users\\user\\Desktop\\my_pythonworks\\function\\country\\data.json"
with open(path,encoding="utf-8") as f:
    data=load(f)
print(len(data))

all_region={c.get("region") for c in data}
print(all_region)

# asian country names
# ---------------------
asia_country=[c.get("name") for c in data if c.get("region")=="Asia"]
print(asia_country)

# independent country
# ----------------------

indep_country=[c.get("name") for c in data if c.get("independent")==True]
print(indep_country)

#contry with hig population
# --------------------------

pop_country=max(data,key=lambda c:c.get("population"))
print(pop_country.get("name"))

#countries that shares border with india
# --------------------------------------

india_borders=[]