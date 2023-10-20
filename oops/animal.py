class animal:

    
    def __init__(self,name):
        self.name=name

    def sounds(self):
        pass

class dog(animal):

    def sounds(self):
        print(f"{self.name} barks")

obj1=dog("dog")
obj1.sounds()

class frog(animal):

    def sound(self):
        print(f"{self.name} croacks")

obj2=frog("frog")
obj2.sounds()


print(obj2.__class__)   #class ethann ariyaan   () closing bracket illengil ath method alla attributann

# __init__
# __str__
# __class__
    

