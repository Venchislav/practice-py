def deleteDuplicates(self, head):
    c = head
    while c:
        while c.next and c.next.val == c.val:
            c.next = c.next.next
        c = c.next
    return head

# Yep... LeetCode... Suddenly)
# Actually it's not even my solution in there, but it's print(' '.join(list('GIGABRAIN')))
