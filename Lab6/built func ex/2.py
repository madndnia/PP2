#Write a Python program with builtin function that accepts a string and calculate 
#the number of upper case letters and lower case letters

def count(x):
    a = 0
    b = 0
    for i in x:
        if i.islower() and i != ' ':
            a += 1
        elif i.isupper() and i != ' ':
            b += 1
    print(f"Number of upper case letters: {a}")
    print(f"Number of lower case letters: {b}")

q = input()
count(q)