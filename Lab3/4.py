"""You are given list of numbers separated by spaces. Write a 
function filter_prime which will take list of numbers as an 
agrument and returns only prime numbers from the list."""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    prime_numbers = []
    for num in numbers:
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

numbers_list = [23, 4, 17, 11, 6, 9, 29, 13]
print(filter_prime(numbers_list)) 