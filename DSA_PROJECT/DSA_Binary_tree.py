class Treenode:
    def __init__(self):
        self.data = self.data
        self.left = None
        self.right = None

root = Treenode('R')
nodeA = Treenode('A')
nodeB = Treenode('B')
nodeC = Treenode('C')
nodeD = Treenode('D')
nodeE = Treenode('E')
nodeF = Treenode('F')
nodeG = Treenode('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

# Test 
print("Root.right.left.data:", root.right.left.data)


