#Write a Python program with builtin function that returns True 
#if all elements of the tuple are true.

mytuple = (1, 0, 1, 2, "madndnia", True, "True")

def a(s):
    security = True
    for i in s:
        if i == False:
            security = False
    print(security)

a(mytuple)
zakonoslyzhnyi = (1,1,1,True,True,True)
a(zakonoslyzhnyi)