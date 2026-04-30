class node:
    def __init__(self, data):
        self.data = data
        self.next = None

    a = node(5)
    b = node(3)
    c = node(7)

    
    a.next = b
    b.next = c

    head = a
    print(head.data)
    print(head.next.data)
    print(head.next.next.data)
    




