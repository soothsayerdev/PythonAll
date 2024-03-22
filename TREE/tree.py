

class TreeNode:
    # Nó da Arvore
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        
    def __str__(self) -> str:
        return str(self.data)
        

class BinaryTree:
    # Arvore Binaria ( 2 filhos OBRIGATORIAMENTE )
    def __init__(self, data = None) -> None:
        if data:
            node = TreeNode(data)
            self.root = node
        else:
            self.root = None
        
    # percurso em ordem simétrica
    def simetric_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            print('(', end='')
            self.simetric_traversal(node.left)
        print(node, end='')
        if node.right:
            self.simetric_traversal(node.right)
            print(')', end='')

    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node)
        
    # Metodo para achar a altura da arvore
    def height(self, node=None):
        if node is None:
            node = self.root
        hleft = 0
        hright = 0
        if node.left:
            hleft = self.height(node.left)
        if node.right:
            hright = self.height(node.right)
        if hright > hleft:
            return hright + 1
        return hleft + 1
                
        
        
if __name__ == "__main__":
#    tree = BinaryTree(7)
#    tree.root.left = TreeNode(18)
#    tree.root.right = TreeNode(14)
#
#    print(tree.root)
#    print(tree.root.right)
#    print(tree.root.left)

    tree = BinaryTree()
    n1  = TreeNode('a')
    n2  = TreeNode('+')
    n3  = TreeNode('*')
    n4  = TreeNode('b')
    n5  = TreeNode('-')
    n6  = TreeNode('/')
    n7  = TreeNode('c')
    n8  = TreeNode('d')
    n9  = TreeNode('e')
    
    n6.left = n7
    n6.right = n8
    n5.left = n6
    n5.right = n9
    n3.left = n4
    n3.right = n5
    n2.left = n1
    n2.right = n3
    
    tree.root = n2
    
    tree.simetric_traversal()
    print()
    
    def postorder_example_tree():
        tree = BinaryTree()
        n1  = TreeNode('I')
        n2  = TreeNode('N')
        n3  = TreeNode('S')
        n4  = TreeNode('C')
        n5  = TreeNode('R')
        n6  = TreeNode('E')
        n7  = TreeNode('V')
        n8  = TreeNode('A')
        n9  = TreeNode('5')
        n0 = TreeNode('3')
        
        n0.left = n6
        n0.right = n9
        n6.left = n1
        n6.right = n5
        n5.left = n2
        n5.right = n4
        n4.left = n3
        n9.right = n8
        n8.left = n7
        
        tree.root = n0
        return tree
    
    if __name__ == "__main__":
        tree = postorder_example_tree()
        print("Percurso em pós ordem:")
        tree.postorder_traversal()
        print("Altura: ", tree.height())