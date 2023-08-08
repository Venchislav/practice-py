from collections import Counter


def majority_element(nums):
    cnt = Counter(nums)
    v, c = cnt.most_common()[0]
    return v
