#Python Lists


#EXAMPLE
thislist = ["apple", "banana", 'cherry']
print(thislist)

#EXAMPLE
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#EXAMPLE
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#EXAMPLE
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#EXAMPLE
list1 = ["abc", 34, True, 40, "male"]

#EXAMPLE
#<class 'list'>
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#EXAMPLE 
thislist = list(("apple", "banana", "cherry")) 
# note the double round-brackets
print(thislist)

"""Python Collections (Arrays) доп инфа 
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members."""


#EXERCISES:

#Print the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
print(fruits[1])


#Change the value from "apple" to "kiwi", in the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits[0]= "kiwi"


#Use the append method to add "orange" to the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")


#Use the insert method to add "lemon" as the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")


#Use the remove method to remove "banana" from the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")


#Use negative indexing to print the last item in the list.
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])


#Use a range of indexes to print the third, fourth, and fifth item in the list.
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])


#Use the correct syntax to print the number of items in the list.
fruits = ["apple", "banana", "cherry"]
print(len(fruits))


