class mobiles:
    data=[
        {"id":100,"name":"galaxya5","price":35000},
        {"id":101,"name":"mi11i","price":25000},
        {"id":102,"name":"iphone15","price":135000},
        {"id":103,"name":"s23","price":145000},
        {"id":104,"name":"neo","price":35000},

    ]

    # list all mobiles
    # print details of a specific mobile
    # update a mobile
    # delete a mobile
    # list,retrive,edit,delete

    # crud- create,retrive,update,delete


#create.............................

    def create(self,*args,**kwargs):
        self.data.append(kwargs)
        return f"{kwargs} created !!!!"
    


      #retrieve............................


    def retrieve(self,id,*args,**kwargs):
        obj=[mob for mob in self.data if mob.get("id")==id].pop()
        return obj
  
    #print all

    def get(self,*args,**kwargs):
        return f"{self.data}"
    
    
    #update.....................
    def put(self,id,*args,**kwargs):
        obj=[mob for mob in self.data if mob.get("id")==id].pop()
        obj.update(kwargs)
        return f"{obj} has been updated"
    

    #delete

    def destroy(self,id,*args,**kwargs):
        # id=kwargs.get("id")
        obj=[mob for mob in self.data if mob.get("id")==id].pop()
        self.data.remove(obj)
        return f"{obj} removed from db"
    




obj=mobiles()
# print(create(id="11011",name="iphone15",price=70000))   #create....
# print(obj.retrieve(id=103))  #retrieve..............
# print(obj.get()) #print all................
# print(obj.put(id=100,name="samsung s23",price=75000))
print(obj.destroy(id=102))

    