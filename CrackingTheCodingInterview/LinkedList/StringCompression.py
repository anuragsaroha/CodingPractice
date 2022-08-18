"""
Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
"""


def str_compression(string):
    n = len(string)
    count = 1
    compressed = ''
    for i in range(n-1):
        if string[i] == string[i+1] and i < n-2:
            count += 1
        elif string[i] == string[i+1] and i == n-2:
            count += 1
            compressed += string[i] + str(count)
        else:
            compressed += string[i] + str(count)
            count = 1

    if len(compressed) > len(string):
        return string
    else:
        return compressed


if __name__ == "__main__":
    print(str_compression('aabcccccdddd'))
    print(str_compression('abcde'))
