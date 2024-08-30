            ####### Detectar Ciclos em um grafo ########

# Dado um Grafo não direcionado, determine se ele contem ciclos

def has_cycle(graph):
    visited = set()
    
    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False
    
    for node in graph:
        if node not in visited:
            if dfs(node, -1):
                return True
    return False

# Caso de uso:
graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1],
    4: [2, 5],
    5: [4, 6],
    6: [5]
}
print(has_cycle(graph)) # OUTPUT : False ( não contém ciclo )
