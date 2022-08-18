# Write a recursive function that returns the sum of the digits of a given integer.
# Input format : Integer N
# Output format : Sum of digits of N
# Sample Input 1 : 12345
# Sample Output 1 : 15
# Sample Input 2 : 9
# Sample Output 2 : 9


def sum_of_digits(num):
    x = len(str(num))
    if x == 1:
        return num
    else:
        digit = num//(10 ** (x-1))
        return digit + sum_of_digits(num - (digit * (10 ** (x-1))))


print(sum_of_digits(87654))