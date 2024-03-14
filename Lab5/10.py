#Write a Python program to convert a given camel case string to snake case.

import re

def a(txt):
    result = re.sub('([a-z])([A-Z])', r'\1_\2', txt)
    return result

s = str(input())
result = a(s)

print("String:", s)
print("Result:", result)