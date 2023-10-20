data=[
        {"id":100,"name":"galaxya5","price":35000},
        {"id":101,"name":"mi11i","price":25000},
        {"id":102,"name":"iphone15","price":135000},
        {"id":103,"name":"s23","price":145000},
        {"id":104,"name":"neo","price":35000},
   ]

# create.......................................

def create(*args,**kwargs):
    data.append(kwargs)
    return f"{kwargs} created succesfully"

print(create(id="11011",name="iphone15",price=70000))

# retrieve.....................................

def retrieve(*args,**kwargs):
    #kwargs={id:100}
    id=kwargs.get("id")
    obj=[mob for mob in data if mob.get("id")==id]
    return obj

print(retrieve(id=101))

#delete............................................

def destroy(*args,**kwargs):
    id=kwargs.get("id")
    obj=[mob for mob in data if mob.get("id")==id].pop()  # evide pop cheyane list inn porathek edukanannn
    data.remove(obj)
    return f"{obj} removed from db"

print(destroy(id=101))



#update............................................

def put(id,*args,**kwargs):
    obj=[mob for mob in data if mob.get("id")==id].pop()
    obj.update(kwargs)
    return f"{obj} has been updated"

print(put(id=100,name="samsung s23",price=75000))

