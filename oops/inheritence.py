#inheritance


class parent:

    def mobile(self):
        print("samsung a52 s1")

    def bike(self):
        print("duke")

class child(parent):
    pass

obj=child()
obj.mobile()
obj.bike()


#------------------------------------------------



class editor:

    name:str
    def __init__(self,name):
        self.name=name

    def spec(self):
        pass

class VsCode(editor):

    def spec(self):
        print(f"{self.name} supports edit,debug,run,extension supports")

    def __str__(self):
        return self.name
    
vobj=VsCode("VsCode")
vobj.spec()
print(vobj)