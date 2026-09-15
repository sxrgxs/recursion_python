def binary_search(k : list, target, l, r):
    if l > r:
        return -1
    m = (l + r)// 2
    if k[m] == target:
        return m
    if k[m] < target:
        return binary_search(k, target, m + 1, r)
    else:
        return binary_search(k, target, l, m - 1)

a = list()
a.extend(map(int, input().split()))
targ = int(input())

print(binary_search(a, targ, 0, len(a) - 1))