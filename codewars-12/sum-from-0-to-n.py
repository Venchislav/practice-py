def show_sequence(n):
    if n > 0:
        return '+'.join([str(i) for i in range(n+1)]) + ' = ' + str(sum(list(range(n)))+n)
    elif n == 0: return '0=0'
    else: return f'{n}<0'
