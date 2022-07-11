"""
Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.
"""


def sq_sorted(arr):
    sq_arr = [0] * len(arr)
    left = 0
    right = len(arr) - 1
    idx = len(arr) - 1
    left_sq = arr[left] ** 2
    right_sq = arr[right] ** 2
    while left <= right:
        if right_sq >= left_sq:
            sq_arr[idx] = right_sq
            right -= 1
            right_sq = arr[right] ** 2
        else:
            sq_arr[idx] = left_sq
            left += 1
            left_sq = arr[left] ** 2
        idx -= 1
    return sq_arr


if __name__ == "__main__":
    print(sq_sorted([-2, -1, 0, 2, 3]))
    print(sq_sorted([-3, -1, 0, 1, 2]))
