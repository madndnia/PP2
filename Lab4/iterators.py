#Python Iterators


#from tuple
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


#from string
mystr = "banana"
myit = iter(mystr) #будет выводить все буквы по отдельности

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


#for "for" loop
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

#for string loop
mystr = "banana"

for x in mystr:
  print(x)


#for classes
class MyNumbers:
  def __init__(self):
    self.a = 1
    return self
  
  def __next__(self):
    x = self.a
    self.a += 1
    return x
  
  myclass = MyNumbers()
  myiter = iter(myclass) 

  print(next(myiter))
  print(next(myiter))
  print(next(myiter))
  print(next(myiter))
  print(next(myiter))

#stop after 20 iterators
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
