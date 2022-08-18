"""
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
"""


def triplet_sum(arr):
    arr.sort()
    triplets = []
    for i in range(len(arr)-2):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        search_pair(arr, i+1, -arr[i], triplets)
    return triplets


def search_pair(arr, left, target, triplets):
    right = len(arr) - 1
    while left < right:
        if arr[left] + arr[right] == target:
            triplets.append([-target, arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left-1]:
                left += 1
            while left < right and arr[right] == arr[right+1]:
                right -= 1
        elif arr[left] + arr[right] > target:
            right -= 1
        else:
            left += 1


if __name__ == "__main__":
    print(triplet_sum([-3, 0, 1, 2, -1, 1, -2]))
    print(triplet_sum([-5, 2, -1, -2, 3]))
