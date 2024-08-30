# Dado um conjunto de numeros inteiros, determine se há um subconjunto cuja soma seja igual a um valor-alvo

def subset_sum(nums, target):
    n = len(nums)
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = True
        
    for i in range(1, n + 1):
        dp[i][0] = True
        
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if nums[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]
    
    return dp[n][target]

# Caso de Uso:
nums = [3, 34, 4, 12, 5, 2]
target = 9
print(subset_sum(nums, target)) # OUTPUT: True ( 4 + 5 = 9)