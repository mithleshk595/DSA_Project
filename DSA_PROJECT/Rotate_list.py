class solution:
    def rotateRight(self, head, k):
        if head == None or head.next == None:
            return head 
        
        l = 0
        last = head
        while last.next!= None:
            last = last.next
            l+=1
        l+=1
        
        k = k%l
        if k == 0:
            return head
        
        curr = head 
        for i in range(k-1-l):
            curr = curr.next
            last = last.next
            last.next = head 
            head = curr.next
            curr.next = None
        return head 
    