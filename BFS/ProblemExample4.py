# Nivel de uma Arvore
# Dada uma arvore binaria, encontre o numero de nós em cada nivel

from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        

def count_nodes_per_lvl(root):
    if not root:
        return 
    
    lvls = []
    queue = deque([root])
    
    while queue:
        lvl_size = len(queue)
        lvl_nodes = []
        
        for _ in range(lvl_size):
            node = queue.popleft()
            lvl_nodes.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
        lvls.append(lvl_nodes)
    
    return lvls    
    
# Exemplo de Uso:
# Construa uma arvore binaria

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(count_nodes_per_lvl(root)) # OUTPUT : [[1], [2, 3], [4, 5, 6, 7]]