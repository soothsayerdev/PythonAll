        #### Encontrar todos os caminhos em um grafo ####
        
# Encontre todos os caminhos entre dois nós em um grafo direcionado

def all_paths(graph, start, end):
    def dfs(node, path):
        if node == end:
            paths.append(path)
            return
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                dfs(neighbor, path + [neighbor])
                visited.remove(neighbor)
                
    paths = []
    visited = set([start])
    dfs(start, [start])
    return paths

# Caso de Uso
graph = {
    1: [2, 3],
    2: [4],
    3: [4],
    4: [5],
    5: []
}
print(all_paths(graph, 1, 5)) # OUTPUT: [[1, 2, 4, 5], [1, 3, 4, 5]]