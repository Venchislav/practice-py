classes = {}


def add_class(clss, cls_name, parents):
    if cls_name not in clss:
        clss[cls_name] = []
    clss[cls_name].extend(parents)
    for prnt in parents:
        if prnt not in clss:
            clss[prnt] = []


def found_path(cls, start, end, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == end:
        return path
    if start not in cls:
        return None
    for node in cls[start]:
        if node not in path:
            new_path = found_path(cls, node, end, path)
            if new_path:
                return new_path
    return None


def answer(clss, prnt, chld):
    if not (prnt or chld) in clss or not found_path(clss, chld, prnt):
        return 'No'
    return 'Yes'


n = int(input())
for _ in range(n):
    class_description = input().split()
    class_name = class_description[0]
    class_parents = class_description[2:]
    add_class(classes, class_name, class_parents)

q = int(input())
for _ in range(q):
    question = input().split()
    parent = question[0]
    child = question[1]
    print(answer(classes, parent, child))
