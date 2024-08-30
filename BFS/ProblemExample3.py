# Encontrar o menor numero de saltos em um labirinto
# Dada uma grade 2D onde 0 é um espaço livre e 1 é um 
# obstaculo, encontre o menor numero de passos para ir do inicio ao fim.

from collections import deque

def min_steps_maze(maze):
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(0, 0, 0)]) # (row, col, steps)
    visited = set((0,0))
    
    while queue:
        row, col, steps = queue.popleft()
        
        if row == rows - 1 and col == cols - 1:
            return steps
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols and maze[new_row][new_col] == 0 and (new_row, new_col) not in visited:
                queue.append((new_row, new_col, steps + 1))
                visited.add((new_row, new_col))
                
    return -1 # Retorna -1 se não for possivel chegar ao destino

# Exemplo de uso:

maze = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 1]
]
print(min_steps_maze(maze)) # OUTPUT: -1

maze = [
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
print(min_steps_maze(maze)) # OUTPUT: 6
                