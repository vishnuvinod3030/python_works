# def add(*args):# * accepts any number of parms in tuple
#     return sum(args)

# print(add(10,20,30))
# print(add(10,20,30,40))


# def product(*args):
#     res=1
#     for n in args:
#         res=res*n
#     return res

# print(product(10,20))
# print(product(1,2,3,4,5))


# def add(*args):

#     res=0
#     for n in args:
#         res=res+n
#     return res

# print(add(10,20))
# print(add(1,2,3,4,5))


# def adder(*args):
#     return sum(args)

# print(adder(10,20))
# print(adder(1,2,3,4,5))


# def concat_string(*args):
#     res=""
#     for st in args:
#         res+=st
#     return res
# print(concat_string("hello","there"))


#str> join()........................

# def concat_string(*args):
#     return '#'.join(args)

# print(concat_string("hello","hai",'hello'))

# def reverse_concat(* args):
# print(reverse_cocat("red","green","blue"))

# lst=["red","green","blue"]
# lst.reverse()
# print(lst)

# def reverse_concat(*args):
#     data=list(args)
#     data.reverse()
#     return " ".join(data)
# print(reverse_concat("red","green","blue"))

# def person_name(**kwargs):#** is represents dictionary...................................
#     print(kwargs)
# person_name(first_name="sachin",middle_name="ramesh",last_name="tendulkar")

# def empdetails(**kwargs):
#     print(kwargs)
#     name=kwargs.get("name")
#     exp=kwargs.get("exp")
#     dep=kwargs.get("dep")                               #kwarg..............................             #
#     print(f"{name} has {exp} year exp in {dep}")

# empdetails(name="john",exp="2",dep="web devolpment")


def balance_enq(**kwargs):
    print(kwargs)
    b_name=kwargs.get("bank_name")
    acno=kwargs.get("acno")
    bal=kwargs.get("balance")
    print(f"your {b_name} {acno} account balance is INR {bal}")

balance_enq(bank_name='sbi',acno='12334',balance=235455)




def perform_operation(*args,**kwargs):
    num1,num2=args
    op=kwargs.get("operand")
    if op=="+":
        return num1+num2
    elif op=="-":
        return num1-num2
    elif op=="*":
        return num1*num2
    else:
        return "invalid operand"
    
print(perform_operation(10,20,operand="*"))