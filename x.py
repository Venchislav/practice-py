objects = [1, 1, 2, 3, 4, 5, 5]
x = set()
ans = 0
for obj in objects:
    x.add(id(obj))

ans = len(x)

print(ans)

# 5
