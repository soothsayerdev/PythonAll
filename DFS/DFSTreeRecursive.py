class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
def dfs_recursive(root: TreeNode):
    if not root:
        return
    
    print(root.val, end = " ") # Visita o nó
    
    dfs_recursive(root.left) # Realiza a busca em profundidade para o nó esquerdo
    dfs_recursive(root.right) # Realiza a busca em profundidade para o nó direito
    
    
    
    
# Caso de Uso
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

dfs_recursive(root) # OUTPUT: 1 2 4 5 3 6 7
