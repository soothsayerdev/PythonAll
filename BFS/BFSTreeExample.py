from collections import deque

# Aplicações de BFS
# - Encontrar o caminho mais curto em grafos não ponderados
# - Travessia de arvores por niveis
# - Soluçoes de problemas de conectividade em grafos
# - Roteamento de pacotes em redes

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        

def bfs(root: TreeNode):
    if not root:
        return 
    
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        print(node.val, end = " ")
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
            
            

# Caso de Uso
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

bfs(root) # OUTPUT - 1 2 3 4 5 6 7
