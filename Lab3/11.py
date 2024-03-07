
"""Write a Python function that checks whether a word or 
phrase is palindrome or not. Note: A palindrome is word, phrase, 
or sequence that reads the same backward as forward, e.g., madam"""

def palindr():
    word = input()
    word1 = word[::-1]
    if word1 == word:
        print('Это палиндром')
    else:
        print('Это не палиндром')

palindr()
