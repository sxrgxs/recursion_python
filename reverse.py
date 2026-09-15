def reverse(k : list, l, r) -> None:
    if l >= r:
        return
    k[l], k[r] = k[r], k[l]
    reverse(k, l+1, r-1)

a = list()
a.extend(map(int, input().split()))
reverse(a, 0, len(a) - 1)
print(a)