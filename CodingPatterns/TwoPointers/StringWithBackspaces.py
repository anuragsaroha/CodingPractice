"""
Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal.
"""


def is_equal(str1, str2):
    str1_counter = len(str1) - 1
    str2_counter = len(str2) - 1
    while str1_counter and str2_counter > 0:

        if str1[str1_counter] == "#":
            count = get_next_valid_char(str1, str1_counter)
            str1_counter -= count * 2

        if str2[str2_counter] == "#":
            count = get_next_valid_char(str2, str2_counter)
            str2_counter -= count * 2

        if str1[str1_counter] == str2[str2_counter]:
            str1_counter -= 1
            str2_counter -= 1
        else:
            return False
    return True


def get_next_valid_char(string, counter):
    count = 0
    while string[counter] == '#':
        count += 1
        counter -= 1
    return count


def main():
    print(is_equal("xy#z", "xzz#"))
    print(is_equal("xy#z", "xyz#"))
    print(is_equal("xp#", "xyz##"))
    print(is_equal("xywrrmp", "xywrrmu#p"))


main()
