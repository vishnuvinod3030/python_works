# constructor
# ''''''''''''''
# when object create,instance variable is intialize by contructor

# c++ ,java costructer intialize by its className
# python contructor is __init__
#tostring() object string representaion__str__
# def__str__(self)
#     return self.name

# __init__
# __str__
# __class__



#  * inheritance(single inheritance,multiple inheritance,multilevel inheritance)
#  * polymorphism
#        * method overriding
#        * method overloading
#  * abstraction






class Book:
    name:str
    author:str
    price:float
    publisher:str

    def set_book(self,name,author,price,publisher):
        self.name=name
        self.author=author
        self.price=price
        self.publisher=publisher

    def display(self):
        print(self.name,self.author,self.price,self.publisher)

    def __str__(self):
        return self.name

book1=Book()
book1.set_book("Wings of fire","APJ",500,"DC books")
book1.display()
print(book1)