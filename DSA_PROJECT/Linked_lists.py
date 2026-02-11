class node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traseAndprint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end= " ->")
        currentNode = currentNode.next
    print("null")

def deletespecificnode(head, position):
    if position == 0:
        return head.next
    currentNode = head
    for i in range(position -1):
        if currentNode is None:
            return head
        currentNode = currentNode.next
        if currentNode is None or currentNode.next is None:
            return head
        currentNode.next = currentNode.next.next
        node1 = node(7)
        node2 = node(14)
        node3 = node(21)
        node4 = node(28)
        node5 = node(35)

        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5

        print("Linked list before delection:")
        traseAndprint(node1)
        position = 2 
        node = deletespecificnode(node1, position=position)
        print(f"linked list after deleting node at position {position}:")
        traseAndprint(node)
        

