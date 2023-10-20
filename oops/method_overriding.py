class parent:
    def mobile(self):
        print("samsung s23")

    def car(self):
        print("swift")

class child(parent):  #child parent classine inherit cheythu
    def mobile(self): # evide method overriding cheythu
        print("iphone")

ch=child()
ch.mobile()
ch.car()
