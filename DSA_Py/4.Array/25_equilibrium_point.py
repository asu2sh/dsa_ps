def check_equilibrium(arr):
    n = len(arr)
    for i in range(n):
        left_sum, right_sum = 0, 0
        for j in range(0, i):
            left_sum += arr[j]
        for k in range(i+1, n):
            right_sum += arr[k]
        if left_sum == right_sum:
            return True
    return False


def chk_equilibrium(arr):
    n = len(arr)
    left_sum, right_sum = 0, 0
    
    for i in range(n):
        right_sum += arr[i]

    for i in range(n):
        right_sum -= arr[i]
        if left_sum == right_sum:
            return True
        left_sum += arr[i]
    return False


arr = list(map(int, input().split()))
print(check_equilibrium(arr), chk_equilibrium(arr))