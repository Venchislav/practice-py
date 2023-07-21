def generateShape(integer):
    return '\n'.join('+' * integer for i in range(integer))

# but it's not my code (it's a shorter version) My code is:

def generate_shape(n):
    res = ''
    for i in range(n):
        res += '+' * n + '\n'
    return res[:-1]

# longer, but with close idea
