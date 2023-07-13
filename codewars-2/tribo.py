def tribonacci(signature, n):
    if n == 0:
        return []
    if n < 3:
        return [signature[i] for i in range(0, n)]
    res = signature[:]
    for i in range(3, n):
        res.append(res[i - 1] + res[i - 2] + res[i - 3])
    return res


# But it's pretty hardcoded...
# So it's a way better

def tribonacci(signature, n):
    res = signature[:n]
    for i in range(n - 3): res.append(sum(res[-3:]))
    return res
