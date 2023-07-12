def first_non_consecutive(arr):
    for i in range(len(arr)):
        if arr[i] - arr[i-1] > 1:
            return arr[i]
