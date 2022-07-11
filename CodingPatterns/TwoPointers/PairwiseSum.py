"""
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

"""


# Using 2 pointers


def pair_with_target_sum(arr, target_sum):
    start = 0
    end = len(arr) - 1
    while start < end:
        if arr[start] + arr[end] == target_sum:
            return [start, end]
        elif arr[start] + arr[end] > target_sum:
            end -= 1
        else:
            start += 1
    return [-1, -1]


# Using HashTable

def pair_with_target_sum_hash(arr, target_sum):
    elem_dict = {}
    for index, num in enumerate(arr):
        if (target_sum - num) in elem_dict:
            return [elem_dict[target_sum - num], index]
        else:
            elem_dict[num] = index
    return [-1, -1]


if __name__ == "__main__":
    print(pair_with_target_sum([1, 2, 3, 4, 6], 6))
    print(pair_with_target_sum([2, 5, 9, 11], 11))
    print(pair_with_target_sum_hash([1, 2, 3, 4, 6], 6))
    print(pair_with_target_sum_hash([2, 5, 9, 11], 11))
