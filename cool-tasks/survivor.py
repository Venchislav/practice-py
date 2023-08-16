def task(n, k):
    people = range(1, n+1)
    while len(people) > 1:
        people = people[0:len(people):k]
    return people[0]


print(task(9, 3))
