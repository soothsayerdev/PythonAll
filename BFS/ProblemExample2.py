# Dado um grafo, verifique se ele é conexo

from collections import deque

def is_connected(graph):
    if not graph:
        return True
    
    start_node = next(iter(graph))
    queue = deque([start_node])
    visited = set([start_node])
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    
    return len(visited) == len(graph)


# Exemplo de uso

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}
print(is_connected(graph)) # OUTPUT - TRUE
