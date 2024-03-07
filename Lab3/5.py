"""Write a function that accepts string 
from user and print all permutations of that string."""

def strPermut():
     word = input()
     perm = permut(word)
     for i in list(perm):
         print(i)