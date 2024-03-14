#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

import re

txt = str(input())
x = re.findall("ab*", txt)


print(x)