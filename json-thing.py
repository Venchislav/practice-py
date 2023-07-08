import json
json_txt = input()
res = {}
pythoned_json = json.loads(json_txt)

for elem in pythoned_json:
    for x in elem['parents']:
        if elem['parents'].count(x) == 0:
            res[x] = 1
        if x in res:
            res[x] += 1
        else:
            res[x] = elem['parents'].count(x) + 1

for key in res:
    print(res)
