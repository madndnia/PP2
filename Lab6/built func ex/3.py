#Write a Python program with builtin function that 
#checks whether a passed string is palindrome or not.

def palindr(s):
    pal = ''.join(reversed(s))
    if pal == s:
        print("Palindorme")
    else:
        print("Not palindrome")



q = input()
palindr(q)