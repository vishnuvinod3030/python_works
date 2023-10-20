# # child classil parentinte vehiclesinte koode "ola" add cheyanam



# class parent:
#     def vehicles(self):
#         self.context=["duke","benz"]
#         return self.context

# class child(parent):

#     def vehicles(self):
#         self.context=super().vehicles()     #super class means from parent class
#         self.context.append("ola")
#         return self.context
    
# p=parent()
# print(p.vehicles())

# c=child()
# print(c.vehicles())

# #--------------------------------------------------------------------------------------------



class superheros:
    def __init__(self,name):
        self.name=name

    def super_powers(self):
        self.context["run","jump"]
        return self.contex
    
class spiderman(superheros):
    def super_powers(self):
        self.context=super().super_powers()
        self.context.append("fly")
        self.context.append("web")
        return self.context
    
obj=spiderman("spiderman")
print(obj.super_powers())


        
