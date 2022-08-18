# Given a string S, compute recursively a new string where identical chars that are adjacent in the
# original string are separated from each other by a "*".
# Input format : String S
# Output format : Modified string
# Constraints : 0 <= |S| <= 1000
# where |S| represents length of string S.
# Sample Input 1 :
# hello
# Sample Output 1:
# hel*lo
# Sample Input 2 :
# aaaa
# Sample Output 2 :
# a*a*a*a


def string_recursion(s):
    new_string = ''
    if len(s) == 0:
        return -1
    if len(s) == 1:
        return s
    modified_string = recurse_helper(s, new_string)
    return modified_string


def recurse_helper(s, new_string):
    if len(s) > 1:
        new_string += s[0]
        if s[0] == s[1]:
            new_string += '*'
        return recurse_helper(s[1:], new_string)
    else:
        new_string += s
        return new_string


modified = string_recursion('hello')
print(modified)


# new_string = ''
# index = 0
#
#
# def string_recursion(s):
#     global new_string, index
#     if index < len(s) - 1:
#         new_string += s[index]
#         if s[index] == s[index+1]:
#             new_string += '*'
#         index += 1
#         return string_recursion(s)
#     else:
#         new_string += s[index]
#         return new_string
#
#
# modified = string_recursion('aaaaa')
# print(modified)
