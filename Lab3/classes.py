#Classes

class MyClass:
    x = 5

#Creat 
    

#EXAMPLE 1:

class Strings:
    def getString(self):
        self.word = input()
    def printString(self):
        print(self.word.upper())

s = Strings()
s.getString()
s.printString()




class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()


class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

p1.age = 40


del p1.age

del p1
#exercise
class Person:
  pass


class MyClass:
  x = 5

class MyClass:
  x = 5
p1 = MyClass


class MyClass:
  x = 5
p1 = MyClass

class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)


#class Person:
 # def 
_#_init__
#(self, name, age):
  #  self.name = name
  #  self.age = age