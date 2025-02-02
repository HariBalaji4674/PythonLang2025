print("Object Oriented Programming Language")
print("Python support object and structured")

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

class mainClass:
    def myNew(self):
        print("Peddireddy")

mainClass.myNew(self=" ")

class bank_account:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance+amount
        print(f"{amount} has been added to account")

    def total(self):
        print(self.balance)

acc = bank_account("hari",4500)
acc.deposit(6000)
acc.total()



