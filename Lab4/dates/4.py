#Write a Python program to calculate two date difference in seconds.

from datetime import datetime

date1 = datetime(2007, 10, 28, 0, 0)
date2 = datetime(2005, 9, 6, 0, 0)

time_dif = date2 - date1

x = time_dif.total_seconds()
print(x)