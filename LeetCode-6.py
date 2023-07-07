def deleteDuplicates(head):
    for elem in head:
        for i in range(head.count(elem) - 1):
            head.remove(elem)
    return sorted(head)


print(deleteDuplicates([1, 1, 2, 3, 3]))
