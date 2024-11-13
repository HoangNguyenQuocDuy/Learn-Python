nums = [1, 9, 10, 20, 30, -9, 8, -2, 6]

def linearSearch(arr, target):
    for idx in range(len(arr)):
        if arr[idx] == target:
            return idx

    return -1


# print(linearSearch(nums, 2))
