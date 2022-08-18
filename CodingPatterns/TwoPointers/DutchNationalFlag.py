"""
Given an array containing 0s, 1s and 2s, sort the array in-place.
You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.
"""


def dnf(arr):
    z_idx = 0
    t_idx = len(arr) - 1
    i = 0
    while i <= t_idx:
        if arr[i] == 1:
            i += 1
        elif arr[i] == 0:
            arr[i], arr[z_idx] = arr[z_idx], arr[i]
            i += 1
            z_idx += 1
        else:
            arr[i], arr[t_idx] = arr[t_idx], arr[i]
            t_idx -= 1
    return arr


if __name__ == "__main__":
    print(dnf([1, 0, 2, 1, 0]))
    print(dnf([2, 2, 0, 1, 2, 0]))
