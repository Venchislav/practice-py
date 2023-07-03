def get(namesp, arg):
    if arg in scopes[namesp]['variables']:
        print(namesp)
    elif arg not in scopes[namesp]['variables'] and namesp != 'global':
        namesp = scopes[namesp]['parent']
        get(namesp, arg)
    elif arg not in scopes[namesp]['variables'] and namesp == 'global':
        print(None)


scopes = {'global': {'parent': None, 'variables': set()}}
n = int(input())

for i in range(n):
    cmd, namesp, arg = input().split()
    if cmd == 'create':
        scopes[namesp] = {'parent': arg, 'variables': set()}
        scopes[arg]['variables'].add(namesp)
    elif cmd == 'add':
        scopes[namesp]['variables'].add(arg)
    elif cmd == 'get':
        get(namesp, arg)