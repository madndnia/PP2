"""Write a function that accepts string from user, return a
 sentence with the words reversed. We are ready -> ready are We"""

def wordRev():
    word = input()
    a = word.split()
    a = list(a)
    a.reverse()
    x = ' '.join(a)
    print(x)

wordRev()