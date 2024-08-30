# Dado um numero infinito de moedas de valores diferentes, determine o numero minimo de moedas necessarias para formar um valor-alvo

def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
            
    
    return dp[amount] if dp[amount] != float('inf') else - 1

# Caso de uso
coins = [1, 2, 5]
amount = 11
print(coin_change(coins, amount)) # OUTPUT: 3 (11 = 5+5+1)