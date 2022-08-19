# Write a recursive method, named isPrime() that checks if a number is prime or not.

import math


def is_prime(num):
    if num <= 1:
        return -1
    divisor_list = range(2, math.floor(math.sqrt(num)+1))
    return prime_helper(num, divisor_list)


def prime_helper(num, divisor_list):
    if len(divisor_list) == 0:
        return True
    if num % divisor_list[0] == 0:
        print("The number is not prime and is divisible by {divisor}".format(divisor=divisor_list[0]))
        return False
    else:
        return prime_helper(num, divisor_list[1:])


print(is_prime(29))