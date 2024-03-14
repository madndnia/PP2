#Write a Python program to print yesterday, today, tomorrow.

from datetime import datetime, timedelta

b = today = datetime.now()

a = yesterday = today - timedelta(days=1)
c = tomorrow = today + timedelta(days=1)

print(a)
print(b)
print(c)