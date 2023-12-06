def max_appearing_in_ranges(left, right, n):
    freq = [0] * 101
    for i in range(n):
        freq[left[i]] += 1
        freq[right[i]+1] -= 1
    
    res = 0
    for i in range(1, 100):
        freq[i] += freq[i-1]
        if freq[i] > freq[res]:
            res = i
    return res


lft = [1, 2, 4]
ryt = [4, 5, 7]
n = len(lft)
print(max_appearing_in_ranges(lft, ryt, n))