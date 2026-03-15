class TreeNode:
    def __init__(self):
        self.data = self.data
        self.left = None
        self.right = None

def inOrder_traversal(node):
    if node is not None:
        inOrder_traversal(node.left)
        print(node.data, end='')
        inOrder_traversal(node.right)

root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG


# Traverse 
inOrder_traversal(root)
