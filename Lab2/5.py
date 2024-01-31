#Python Sets

#EXAMPLES:

#Create a Set:
thisset = {"apple", "banana", "cherry"}
print(thisset)

#Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#True and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#False and 0 is considered the same value:
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)


#Get the number of items in a set:
thisset = {"apple", "banana", "cherry"}

print(len(thisset))


#Set items can be of any data type:

#Example
#String, int and boolean data types:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#A set with strings, integers and boolean values:
set1 = {"abc", 34, True, 40, "male"}


#What is the data type of a set?
myset = {"apple", "banana", "cherry"}
print(type(myset))


#Using the set() constructor to make a set:
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)



#EXERCISES

#Use the add method to add "orange" to the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")


#Use the correct method to add multiple items (more_fruits) to the fruits set.
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)


#Use the remove method to remove "banana" from the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")


#fruits = {"apple", "banana", "cherry"}
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")













