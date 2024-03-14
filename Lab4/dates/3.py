#Write a Python program to drop microseconds from datetime.

from datetime import datetime

timenow = datetime.now()
x = timenow.replace(microsecond=0)
print(x)

#replace - заменить