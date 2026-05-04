class solution:
    def deleteDuplicates(self, head):
        # corner cases
        if head==None or head.next!=None:
            return head
        
        curr = head
        while curr.next!=None:
            if curr.next.val == curr.val:
                curr.next = curr.next.next

            else:
                curr = curr.next

        return head
    
