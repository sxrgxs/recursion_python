def power(x,n):
    if n == 0:
        return 1
    part = power(x, n//2)
    result = part * part
    if n%2 != 0:
        result *= x
    return result

x, n = map(int, input().split())

print(power(x, n))

# Time: O(logn) Space: O(logn)