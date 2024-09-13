import sys

class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action
        
class StackFrontier:
    
    def __init__(self) -> None:
        self.frontier = []
        
    def add(self, node):
        self.frontier.add(node)
    
    def remove(self):
        if self.empty():
            raise Exception("A pilhas está vazia!")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node 
    
    def empty(self):
        return len(self.frontier) == 0   

    def contains(self, state):
        return any(node.state == state for node in self.frontier)

        # exists = False
        
        for node in self.frontier:
            if node.state == state:
                # exists = True
                return True
        
        return False
    

class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("A fila está vazia!")
        else:
            # node = self.frontier.pop(0)
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
    
    

class Maze:
    
    def __init__(self):
        maze = [[]]
        pass
    
    def neighbors(self, state):
        row, col = state # linha, coluna = estado
        candidates = [
            ("up", (row - 1, col)), 
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]
        result = []
        for action, (r, c) in candidates:
            if 0 <= r <= self.height and 0 <= c <= self.width
            result.append((action, (r, c)))
        
    
    def solve(self):
        """
            Encontrar, se existir, a soluçao para o labirinto
        """
        
        self.n_explored = 0
        start = Node(state = None, parent = None, action = None)
        frontier = StackFrontier() # Busca em Profundidade 
        # frontier = QueueFrontier() # Busca em Largura
        frontier.add(start)
        self.explored = set()
        
        self.explored = set()
        
        while True:
            if frontier.empty():
                raise Exception("Não há solução para esse labirinto!")    
            pass