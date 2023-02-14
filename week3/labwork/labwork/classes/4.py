class Point:
  def __init__(self,x,y):
    self.x = x
    self.y = y

  def move(self,d,e):
    self.x = self.x+d
    self.y= self.y+e
    return self.x,self.y
  def distance(self,a,b):

    self.x = self.x - a
    self.y = self.y - b
    return (self.x**2 + self.y**2)**1/2
  
    

a=int(input())
b=int(input())
c=Point(a,b)
d=int(input())
e=int(input())
c.move(d,e)
print(c.distance(a,b))