class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, l,wi):
        Shape.__init__(self)
        self.length = l
        self.width = wi

    def area(self):
        return self.length*self.width
a=int(input())
b=int(input())
c = Rectangle(a,b)
print(c.area())