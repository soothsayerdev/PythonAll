from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def dfs_iterative(root: TreeNode):
    if not root:
        return
    
    stack = deque([root])
    
    while stack:
        node = stack.pop()
        print(node.val, end = " ") # Visita o nó
        
        # Adiciona o filho direito primeiro para que o filho esquerdo seja processado primeiro
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
            


# Caso de Uso
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
dfs_iterative(root) # OUTPUT: 1 2 4 5 3 6 7  


""" 
    1
   / \
  2   3
 / \ / \
4  5 6  7

"""
        