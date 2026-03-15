class TreeNode:
    def __int__(self):
        self.data = self.data
        self.left = None
        self.right - None
        def postOrder_traversal(Node):
            if Node is not None:
                postOrder_traversal(Node.left)
                postOrder_traversal(Node. right)
                print(Node.data, end='')

rootA = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')

rootA.left = nodeA
rootA.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

print("post-order traversal of the tree is :")


