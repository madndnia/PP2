"""Write a program to solve a classic puzzle: We count 35 heads 
and 94 legs among the chickens and rabbits in a farm. How many 
rabbits and how many chickens do we have? create function:
solve(numheads, numlegs):"""

def solve(numheads, numlegs):
    rabbit = (numlegs - 2 * numheads) / 2 
    chicken  = numheads - rabbit
    return chicken, rabbit

numheads = 35
numlegs = 94

print(solve(numheads, numlegs))