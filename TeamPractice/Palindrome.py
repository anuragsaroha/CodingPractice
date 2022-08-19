# Recursively find out whether a string is a palindrome.


def is_palindrome(input_string):
    if len(input_string) <= 1:
        return True
    left = 0
    right = len(input_string) - 1
    if input_string[left] == input_string[right]:
        return is_palindrome(input_string[left+1:right])
    else:
        return False


print(is_palindrome('rotator'))
print(is_palindrome('madam'))
print(is_palindrome('truncate'))
print(is_palindrome('racecar'))


def is_palindrome_phrase(input_phrase):
    if len(input_phrase) <= 1:
        return True
    left = 0
    right = len(input_phrase) - 1
    if input_phrase[left] == ' ':
        return is_palindrome_phrase(input_phrase[left+1:])
    elif input_phrase[right] == ' ':
        return is_palindrome_phrase(input_phrase[:right])
    elif input_phrase[left] == input_phrase[right]:
        return is_palindrome_phrase(input_phrase[left+1:right])
    else:
        return False


print(is_palindrome_phrase('taco cat'))
print(is_palindrome_phrase('never odd or even'))
