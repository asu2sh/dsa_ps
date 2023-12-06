def getSum(arr, l, r):
    if l == 0:
        return arr[r]
    return arr[r] - arr[l-1]


arr = list(map(int, input().split()))
l, r = int(input()), int(input())

# Precompute PrefixSum Array
s = arr[0]
for i in range(1, len(arr)):
    s += arr[i]
    arr[i] = s

print(getSum(arr, l, r))
