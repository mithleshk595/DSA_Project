
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverse(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")


node1 = node(7)
node2 = node(14)
node3 = node(21)
node4 = node(28)
node5 = node(35)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

traverse(node1)





