# Given an array of length N and an integer x, you need to find if x is present in the array or not.
# Return true or false.
# Input Format : Line 1 : An Integer N i.e. size of array
# Line 2 : N integers which are elements of the array, separated by spaces
# Line 3 : Integer x
# Output Format :'true' or 'false'
# Constraints : 1 <= N <= 10^3
# Sample Input 1 :
# 3
# 9 8 10
# 8
# Sample Output 1 :
# true
# Sample Input 2 :
# 3
# 9 8 10
# 2
# Sample Output 2 :
# false


def is_present(length, array, elem):
    if length == 0:
        return False
    if array[0] == elem:
        return True
    else:
        return is_present(length-1, array[1:], elem)


print(is_present(3, [9,8,10], 8))
print(is_present(3, [9,8,10], 2))