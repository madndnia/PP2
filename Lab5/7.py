#Write a python program to convert snake case string to camel case string

import re

def a():
    txt = input()
    x = txt.split("_")
    for i in range(1, len(x)):
        x[i] = x[i].capitalize()
    for i in x:
        print(i, end ='')
a()
    
