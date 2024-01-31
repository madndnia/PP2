                                #EXAMPLES

#Boolean Values

"""In programming you often need to know if an expression is True or False.
You can evaluate any expression in Python, and get one of two answers, True or False.
When you compare two values, the expression is evaluated and Python returns the Boolean answer:"""

  #EXAMPLE 1

print(10 > 9)
print(10 == 9)
print(10 < 9)

#When you run a condition in an if statement, Python returns True or False:

  #EXAMPLE 2
"""Print a message based on whether the condition is True or False:"""

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


#The bool() function allows you to evaluate any value, and give you True or False in return,
  
  #EXAMPLE 3
#Evaluate a string and a number:
print(bool("Hello"))
print(bool(15))

  #EXAMPLE 4
#Evaluate two variables:

x = "Hello"
y = 15

print(bool(x))
print(bool(y))


"""Most Values are True
Almost any value is evaluated to True if it has some sort of content.
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones."""

  #EXAMPLE 5
#The following will return True:

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#Some Value are False
"""In fact, there are not many values that evaluate to False, except empty values, such as (),
[], {}, "", the numver 0, and the value None. And of course the value False evaluates to False."""

  #EXAMPLE 6
#The following will return False:

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


"""One more value, or object in this case, evaluates to False, and that is if you have an object
that is made from a class with a __len__ function that returns 0 or False:"""

  #EXAMPLE 7

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))


#Function can Return a Boolean
#You can creat function that returns a Boolean Value:

  #EXAMPLE 8
#Print the answear of a function:
def myFunction() :
  return True

print(myFunction())

"""You can execute code based on the Boolean answear of a function:"""

  #EXAMPLE 9
#Print "YES!" if the function returns True, otherwise print "NO!":

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")


"""Python a;so has many built-in function that return a boolean value, like the isistance() function,
which can be used to determine if an object is of a certain data type:"""

  #EXAMPLE 10
#Check if an object is on integer or not:

x = 200
print(isinstance(x, int)) 
"""Функция isinstance() проверяет, является ли объект (первый аргумент) экземпляром
                            или подклассом класса classinfo (второй аргумент).яяяяяяяя """


#EXERCISES:

 #The statement below would print a Boolean value, which one?

print(10 > 9)

True


#EXERCISES


#The statement below would print a Boolean value, which one?
print(10 > 9)

True


#The statement below would print a Boolean value, which one?
print(10 == 9)

False


#The statement below would print a Boolean value, which one?
print(10 < 9)

False


#The statement below would print a Boolean value, which one?
print(bool("abc"))

True


#The statement below would print a Boolean value, which one?
print(bool(0))

False


