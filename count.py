def count(s, t):
    count = 0
    for i in range(len(s)):
        if s[i:i+len(t)] == t:
            count += 1
    return count


print(count('abababa', 'aba'))
