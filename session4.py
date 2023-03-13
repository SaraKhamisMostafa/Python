'''class calc:
    def __init__(self,name):
        print(f"welcome{name}")
    def sum(self,x,y):
        print(x+y)
class scicalc(calc):
    def pow(self,x,y):
        print(x**y)    
        



c =calc('sara')
c.sum(9,8)

c1= scicalc('sara')
c1.sum(33,2)

c1.pow(3,2)

d= calc('sama')
d.sum(5,7)'''


class user:
    
    def __init__(self,name,age,gender):
        print(f" welcome {name}")
        self.balance=0
        self.name=name
        self.age=age
        self.gender=gender


    def show_details(self):
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"gender: {self.gender}")    
    
class Bank(user):
    def deposite(self,amount):
        self.balance += amount
        self.show_balance()
    def withdraw(self,amount):
        if amount > self.balance:
            print("you dont have enough balance")
            return
        self.balance -=amount
        self.show_balance()


    def show_balance(self):
        print(f"you current balance is :{self.balance}")
  

u1=Bank('ahmed',33,'male')
u1.deposite(400)
u1.withdraw(800)
u1.show_balance()
u1.show_details()

        
        
