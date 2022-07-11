"""
Given an array of sorted numbers, remove all duplicate number instances from it in-place,
such that each element appears only once.
The relative order of the elements should be kept the same, and
you should not use any extra space so that the solution have a space complexity of O(1).

Move all the unique elements at the beginning of the array and after moving return the length of the subarray
that has no duplicate in it.
"""


def remove_duplicates(arr):
    non_dup_idx = 1
    for idx in range(len(arr)):
        if arr[idx] != arr[non_dup_idx - 1]:
            arr[non_dup_idx] = arr[idx]
            non_dup_idx += 1
    return arr[:non_dup_idx], non_dup_idx


'''
Problem 2: Given an unsorted array of numbers and a target ‘key’, remove all instances of ‘key’ in-place 
and return the new length of the array.
'''


def remove_num(arr, key):
    non_key = 0
    for idx in range(len(arr)):
        if arr[idx] != key:
            arr[non_key] = arr[idx]
            non_key += 1
    return arr[:non_key], non_key


if __name__ == "__main__":
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))
    print(remove_num([3, 2, 3, 6, 3, 10, 9, 3], 3))
    print(remove_num([2, 11, 2, 2, 1], 2))




