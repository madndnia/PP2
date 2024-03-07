
"""Write a Python function that takes a list and returns
 a new list with unique elements of the first list. 
 Note: don't use collection set."""

def unielem(list):
    list1 = []
    for i in list:
        if i not in list1:
            list1.append(i)
    return list1