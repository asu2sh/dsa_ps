def solve(arr):
    n = len(arr)
    
    pre_sum, s = 0, 0
    for i in range(n):
        s += arr[i]
        
    if s%3 != 0:
        return False
    
    s1 = s//3
    s2 = 2 * s1
    
    flag1, flag2 = False, False
    for i in range(n-1):
        pre_sum += arr[i]
        if pre_sum == s1:
            flag1 = True
        elif pre_sum == s2 and flag1:
            flag2 = True
            break
    
    if flag1 and flag2:
        return True
    return False


arr = list(map(int, input().split()))
print(solve(arr))