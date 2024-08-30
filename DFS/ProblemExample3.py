        ##### Problema das N-Rainhas ####
    
# Resolva o problema das N-Rainhas para um tabuleiro de tamanho N

def solve_n_queens(n):
    def is_valid(board, row, col):
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True
    
    def dfs(row):
        if row == n:
            result.append([''.join('Q' if col == c else '.' for c in range(n)) for col in board])
            return 
        
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                dfs(row + 1)
                board[row] = -1
                
    board = [-1] * n
    result = []
    dfs(0)
    return result

# Caso de uso:
print(solve_n_queens(4)) # OUTPUT: [['.Q..', '...Q', 'Q...', '..Q.'], ['..Q.', 'Q...', '...Q', '.Q..']]    