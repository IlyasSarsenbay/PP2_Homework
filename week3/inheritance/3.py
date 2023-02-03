class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printnam(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printnam()
