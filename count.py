def counter(s, t):
    count = 0
    for i in range(len(s)):
        if s[i:i+len(t)] == t:
            count += 1
    return count


print(counter('abababa', 'aba'))


# No func version:

s = input()
t = input()

count = 0
for i in range(len(s)):
    if s[i:i + len(t)] == t:
        count += 1

print(count)
