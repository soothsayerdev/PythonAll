        #### Encontrar o Ciclo Hamiltoniano em um grafo ####
        
# Verifique se existe um ciclo Hamiltoniano em um grafo

# Um Ciclo Hamiltoniano em um grafo é um ciclo que visita cada vértice exatamente uma vez
# e retorna ao vértice inicial, formando um percurso fechado. 
# Ele não precisa cobrir todas as arestas, apenas garantir que todos os vértices sejam visitados uma única vez 
# antes de retornar ao ponto de partida. O problema de determinar se um grafo contém um ciclo Hamiltoniano é um problema NP-completo, o que significa 
# que não há um algoritmo eficiente conhecido para resolvê-lo em todos os casos.


def has_hamiltonian_cycle(graph):
    def dfs(path):
        if len(path) == len(graph) and path[0] in graph[path[-1]]:
            return True
    
        for neighbor in graph[path[-1]]:
            if neighbor not in path:
                path.append(neighbor)
                if dfs(path):
                    return True
                path.pop()
        
        return False

    for start_node in graph:
        if dfs([start_node]):
            return True
    return False

# Caso de Uso
graph = {
    1: [2, 3],
    2: [1, 3, 4],
    3: [1, 2, 4],
    4: [2, 3]
}
print(has_hamiltonian_cycle(graph)) # OUTPUT : True