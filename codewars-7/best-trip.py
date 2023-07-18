import itertools


def choose_best_sum(t, k, ls):
    combinations = list(itertools.combinations(ls, k))
    sums = [sum(i) for i in combinations]
    sums2 = [i for i in sums if i <= t]
    if sums2 == []:
        best = None
    else:
        best = max([i for i in sums if i <= t])
    return best


# shorter and better:

def choose_best_sum(t, k, ls):
    try:
        return max(sum(i) for i in itertools.combinations(ls, k) if sum(i) <= t)
    except:
        return None
