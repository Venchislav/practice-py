x = open('test.txt', 'r')  # keys = r(read) w(write) a(append to the end)

# READING:

# d = x.read(5)  # arg of chars/signs
# print(d)
# y = x.read()  # no args - read all file
# print(y.splitlines())
# y = x.readline().rstrip()  # read line
# print(y)

for line in x:
    line = line.rstrip()
    print(repr(line))

x.close()

# WRITING

x = open('test1.txt', 'w')
content = ['Hello', 'world', 'peace!']
x.write('\n'.join(content))
x.close()

# APPEND

x = open('test1.txt', 'a')
x.write('\nP.S It was appended!')
x.write('\nP.S P.S It was appended later!')
x.close()

# AND FINALLY

# It's pretty risky to use open()-close() as if we have an error before close() file won't close
# So we can use with construction

print('---------------')

with open('test1.txt', 'a') as x, open('test.txt') as t:
    x.write('\nWell')
    for line in t:
        print(repr(line).rstrip())

# File will be closed automatically


with open('dataset_24465_4 (2).txt') as e, open('new.txt', 'w') as x:
    for elem in reversed(list(e)):
        x.write(elem)
