        ###### Encontrar componentes conectados em um grafo #####

# Dado um grafo não direcionado, encontre todos os componentes conectados.

# O algoritmo de busca em profundidade (DFS) é usado para percorrer todos os vértices de um componente conectado.

def connected_components(graph):
    visited = set()
    components = []
    
    def dfs(node, component):
        visited.add(node)
        component.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, component)
    
    for node in graph:
        if node not in visited:
            component = []
            dfs(node, component)
            components.append(component)
    
    return components


# Caso de uso
graph = {
    1: [2, 3],
    2: [1],
    3: [1],
    4: [5],
    5: [4],
    6: []
        
}
print(connected_components(graph)) # OUTPUT : [[1, 2, 3], [4, 5], [6]]