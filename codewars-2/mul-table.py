def multi_table(number):
    x = ''
    for i in range(10):
        x += f'{i+1} * {number} = {(i+1) * number}\n'
    return x[:-1]

print(multi_table(5))
