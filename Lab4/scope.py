#Python Scope


#ex1
def myfunc():
  x = 300
  print(x)

myfunc()

#ex2
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

#ex3
x = 300

def myfunc():
  print(x)

myfunc()

print(x)

#ex4
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)

#ex5
def myfunc():
  global x
  x = 300

myfunc()

print(x)

#ex6
x = 300

def myfunc():
  global x   #use global to return func again
  x = 200

myfunc() #like return it here

print(x)   #выведется только 200
