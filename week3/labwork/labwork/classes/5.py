class Account:
  def __init__(self,x,y):
    self.owner = x
    self.balance = y

  def deposit(self,d):
      self.balance=self.balance+d
      return self.balance
    
  def withdrawal(self, e):
    if e>self.balance:
      print("Withdrawals may not exceed the available balance")
      return self.balance
    else:
      self.balance=self.balance-e
      return self.balance
  
    

a=input()
b=int(input())
c=Account(a,b)
en=True
while(en==True):
  print("Write \"deposit\" if you want to add money to your balance\n"+"Write\"withdrawal\"if you want to take money from your balance")
  s=input()
  if s=="deposit":
    d=int(input())
    print("Your balance "+str(c.deposit(d)))
    print("Write \"Yes\" if you want to stop transaction\n"+"Write \"No\" if you want to continue transaction")
    si=input()
    if si=="Yes":
      en=False
  elif s=="withdrawal":
    e=int(input())
    print("Your balance "+str(c.withdrawal(e)))
    print("Write \"Yes\" if you want to stop transaction\n"+"Write \"No\" if you want to continue transaction")
    si=input()
    if si=="Yes":
      en=False
