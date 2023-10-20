#function overloading
 #same function name or method bit different number of parameters

class operations:
    def add(self,n1,n2):
        return n1+n2
    def add(self,n1,n2,n3):        #python interpreter language ayond last function mathrann print cheyollu athond evide overloading presakthiilla
        return n1+n2+n3
    def add(self,n1,n2,n3,n4):
        return n1+n2+n3+n4
    
op=operations()
print(op.add(10,20,30,40))



#--------------------------------------------------------------------------------------  
def add(*args):
    return sum(args)   #angane cheyan evide use cheyane *arg function use cheyum
print(add(10,20))
print(add(10,30,20,10))