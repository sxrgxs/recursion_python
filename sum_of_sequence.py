def sum(k, n):
    if n == 0:
        return 0
    return sum(k, n - 1) + k[n - 1]

print(sum([1, 4 ,5, 48, 546 ,4 ,1 ,1, 1,2 ,3, 3], 10))
