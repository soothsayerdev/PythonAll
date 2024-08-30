# Dado um Grafo não ponderado e dois nós
# encontre o caminho mais curto entre eles

from collections import deque

def shortest_path_bfs(graph, start, end):
    queue = deque([(start, [start])])
    visited = set([start])
    
    while queue:
        (node, path) = queue.popleft()
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                if neighbor == end:
                    return path + [neighbor]
                queue.append((neighbor, path + [neighbor]))
                visited.add(neighbor)
                
    return None # Retorna None se não houver caminho



# Caso de Uso
graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6, 7],
    4: [2],
    5: [2],
    6: [3],
    7: [3]
}
print(shortest_path_bfs(graph, 1, 5)) # OUTPUT: [ 1, 2, 5 ]