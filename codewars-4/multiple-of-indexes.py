def multiple_of_index(arr):
    if arr[0] == 0:
        return [0] + [arr[i] for i in range(1, len(arr)) if arr[i] % i == 0]
    else:
        return [arr[i] for i in range(1, len(arr)) if arr[i] % i == 0]
