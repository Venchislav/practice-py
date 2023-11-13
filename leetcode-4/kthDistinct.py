def kthDistinct(arr, k):
  for i in arr:
    if arr.count(i) == 1:
      k -= 1
    if k <= 0:
      return i
  return ""


print(kthDistinct(["d","b","c","b","c","a"], 2))
print(kthDistinct(["aaa","aa","a"], 1))
print(kthDistinct(["a","b","a"], 3))

# P.S: I'm not nerd, but why df all LeetCode problems don't follow PEP-8 rules
# Maybe it's necessary, but it irritates me😡💢
