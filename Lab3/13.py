"""Write a program able to play the "Guess the number" - game,
 where the number to be guessed is randomly chosen between
   1 and 20. This is how it should work when run in a terminal:"""
"""Hello! What is your name?
KBTU

Well, KBTU, I am thinking of a number between 1 and 20.
Take a guess.
12

Your guess is too low.
Take a guess.
16

Your guess is too low.
Take a guess.
19

Good job, KBTU! You guessed my number in 3 guesses!"""

from random import randrange

def guess_the_number():
    gue=0
    name=str(input("Hello! What is your name?\n"))

    print("Well",name, ',',"I am thinking of a number between 1 and 20.")

    number=randrange(1,21)

    while True:
        print("Take a guess")
        guess=int(input())
        if number==guess:
            print("Good job, KBTU! You guessed my number",gue, "in guesses!")
            break
        elif guess<number:
            gue+=1
            print("Your guess is too low.")
        else:
            gue+=1
            print("Your guess is too high.")

# print(guess_the_number())