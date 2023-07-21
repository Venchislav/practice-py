def even_numbers(arr,n):
    res = []
    for elem in arr[::-1]:
        if elem % 2 == 0 and len(res) < n:
            res.append(elem)
    return res[::-1]

# GIGA BRAIN

def even_numbers(arr,n):
    return [i for i in arr if i % 2 == 0][-n:] 
