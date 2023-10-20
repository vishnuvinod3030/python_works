class bank:
    acno:int
    ac_type:str
    balance:int
    bank_name:str="SBI" #static variable aayit declare cheythitond
    person_name:str
    ifsc_code:str


    def __init__(self,acno,ac_type,balance,person_name,ifsc_code):
        self.acno=acno
        self.ac_type=ac_type
        self.balance=balance

        self.person_name=person_name
        self.ifsc_code=ifsc_code

    def display(self):
        print(self.acno,self.ac_type,self.balance,self.bank_name,self.person_name,self.ifsc_code)


# per1=bank(1001,"saving",100000,"john","isgdg")
# per1.display()

# per2=bank(1002,"current",1000651,"favas","iswdgdg")
# per2.display()


# per3=bank(1006,"saving",100455,"hope","iszxcgdg")
# per3.display()


    def withdraw(self,amount):
        if self.balance>amount:
            self.balance -=amount
            print(f"yours {self.bank_name} account debited with amount {amount} aval bal {self.balance}")
        else:
            print("transaction declined.....")

        # your sbi bank account debited with amount aval bal is bal
    def deposite(self,amount):
        self.balance+=amount
        print(f"yours {self.bank_name} account debited with amount {amount} aval bal {self.balance}")
    
    def balance_enq(self):
        print(f"your {self.bank_name} account balance is {self.balance}")


obj=bank(1001,"saving",100000,"john","isgdg")
obj.balance_enq()

obj.withdraw(50000)
obj.deposite(20000)

