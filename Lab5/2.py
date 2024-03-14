#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

import re

txt = str(input())
x = re.findall("abb*b", txt)

print(x)