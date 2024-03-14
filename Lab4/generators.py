#generators and iterators

"""Create a generator that generates the squares of numbers 
up to some number N."""

#N = int(input())  
#mygen = (N**2 for N in range(1, N+1)) 
#for N in mygen:
 #   print(N)

"""Write a program using generator to print the even numbers
 between 0 and n in comma separated form where n is input from console."""

#def even(N):
 #   for i in range(0, N+1, 2):
  #      yield i

#N = int(input())
#out = even(N)
#for i in range(0, N+1, 2):
 #   print(next(out), end = ",")

"""Define a function with a generator which can iterate the numbers,
 which are divisible by 3 and 4, between a given range 0 and n."""

#def dividble(N):
 #   for i in range(N+1):
  #      if i % 3 == 0 or i % 4 == 0:
#            yield i

#n = int(input())
#g = (n // 3) + (n // 4) - (n // 12)
#a = dividble(n)
#for i in range(g+1):
 #   print(next(a))

"""Implement a generator called squares to yield the square of all 
numbers from (a) to (b). Test it with a "for" loop and print each of 
the yielded values."""

#def square(n, m):
 #   for i in range(n, m+1):
  #      yield i ** 2

#num = input()
#nums = num.split()
#n, m = int(nums[0]), int(nums[1])

#a = square(n, m)
#for i in range(n, m+1):
 #   print(next(a))

"""Implement a generator that returns all numbers from (n) down to 0."""

def returned(n):
    for i in range(n, -1, -1):
        yield i

n = int(input())
a = returned(n)

for i in range(n+1):
    print(next(a))
    