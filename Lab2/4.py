#Python Tuples

#EXAMPLES

mytuple = ("apple", "banana", "cherry")

#Create a Tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Tuples allow duplicate values:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#Print the number of items in the tuple:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#One item tuple, remember the comma:
thistuple = ("apple",)
print(type(thistuple))


#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
#tring, int and boolean data types:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#A tuple with strings, integers and boolean values:
tuple1 = ("abc", 34, True, 40, "male")

#What is the data type of a tuple?
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#Using the tuple() method to make a tuple:
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)


#EXERCISES

#Use the correct syntax to print the first item in the fruits tuple.
fruits = ("apple", "banana", "cherry")
print(fruits[0])


#Use the correct syntax to print the number of items in the fruits tuple.
fruits = ("apple", "banana", "cherry")
print(len(fruits))


#Use negative indexing to print the last item in the tuple.
fruits = ("apple", "banana", "cherry")
print(fruits[-1])


#Use a range of indexes to print the third, fourth, and fifth item in the tuple.
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])