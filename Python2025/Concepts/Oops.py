# print("Object Oriented Programming Language")
# print("Python support object and structured")

"""
Oops support In python
1: Class : 
- Collection of variables(attributes) and methods(behaviours)
- Class is a Blue-Print
- Logical Entity
- Does not occupy any space in memory

2: Object : 
- An instance/Entities of class
- Physical Entity
- Occupy Space in memory

3: Function :
- A function is inside the class is called Function

4: Method :
- A function inside the class is called method
- A method by default it will take one argument called self
- Self will represent the present class
- 

3: Inheritance
4: Polymorphism
5: Abstraction
"""

class bank_account:
    def __init__(self,owner = "hari",balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self,owner,amount):
        if self.owner ==  owner:
            self.balance = self.balance+amount
            print(f"{amount} has been added to account")
            self.rem_balance()
        else:
            print("Alert !!! Your name is incorrect")

    def withdrawn(self,owner,amount):
        if self.owner == owner:
            if self.balance > amount:
                self.balance = self.balance-amount
                print(f"{amount} has been withdrawn ")
                self.rem_balance()
            else:
                print(f"Alert !!! You have insufficient Funds,\n Your Current Balance is {self.balance}")
        else:
            print("Alert !!! Your name is incorrect,")

    def rem_balance(self):
        print("The remaining Balance is ",self.balance)

acc = bank_account()
acc.deposit("hari",6000)
acc.withdrawn("hari",6000)

"""
Importing Modules and packages 

"""






