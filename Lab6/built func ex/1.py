#Write a Python program with builtin function to multiply all the numbers in a list

def mult(x):
    a = 1
    for i in x:
        a*= i
    print (a)

q = [3, 5, 7, 9, 7]
mult(q)
