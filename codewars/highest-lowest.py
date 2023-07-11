def high_and_low(numbers):
    nms = numbers.split()
    return f'{max(list(map(int, nms)))} {min(list(map(int, nms)))}'


print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
