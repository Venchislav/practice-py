def rowAndMaximumOnes(mat):
    max_r = 0
    max_i = 0
    for i in range(len(mat)):
        if sum(mat[i]) == max_r:
            max_r = max_r
        else:
            max_r = max(max_r, sum(mat[i]))
            if max_r == sum(mat[i]):
                max_i = i

    return [max_i, max_r]


print(rowAndMaximumOnes([[0,1],[1,0]]))
print(rowAndMaximumOnes([[0,0,0],[0,1,1]]))
print(rowAndMaximumOnes([[0,0],[1,1],[0,0]]))
