#Write a Python program to replace all occurrences of space, comma, or dot with a colon.

import re

def a():
    txt = str(input())
    x = re.sub("\s",":", txt)
    x = re.sub(",",":", x)
    x = re.sub("[.]", ":", x)

    print(x)
a()