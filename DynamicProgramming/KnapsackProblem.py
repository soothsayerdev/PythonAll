def knapsack(w, wt, val, n):
    dp = [[0 for _ in range(w + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, w + 1):
            if wt[i - 1] <= w:
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
            
        return dp[n][w]
    
# Caso de uso
w = 50 # Capacidade da mochila
wt = [10, 20, 30] # Pesos dos itens
val = [60, 100, 120] # Valores dos itens
n = len(val)
print(knapsack(w, wt, val, n)) # OUTPUT: 