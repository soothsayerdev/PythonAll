# Voce esta subindo uma escada. Cada vez voce pode subir 1 ou 2 degraus
# De quantas maneiras diferentes voce pode alcançar o topo de uma escada de 'n' degraus?

def climb_stairs(n):
    if n == 1:
        return 1
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        
    return dp[n]

# Caso de Uso:
n = 5
print(climb_stairs(n)) # OUTPUT: 8