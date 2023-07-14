# My solution

def dirReduc(arr):
    dirs = {"WEST": "EAST", "SOUTH": "NORTH", "EAST": "WEST", "NORTH": "SOUTH"}
    res = []

    for i in arr:
        if len(res) == 0 or res[-1] != dirs[i]:
            res.append(i)
            continue
        res.pop()
    return res


# Others good solutions


def dirReduc(arr):
    dir = " ".join(arr)
    dir2 = dir.replace("NORTH SOUTH", '').replace("SOUTH NORTH", '').replace("EAST WEST", '').replace("WEST EAST", '')
    dir3 = dir2.split()
    return dirReduc(dir3) if len(dir3) < len(arr) else dir3


def dirReduc(arr):
    opposites = [{'NORTH', 'SOUTH'}, {'EAST', 'WEST'}]

    for i in range(len(arr) - 1):
        if set(arr[i:i + 2]) in opposites:
            del arr[i:i + 2]
            return dirReduc(arr)

    return arr
