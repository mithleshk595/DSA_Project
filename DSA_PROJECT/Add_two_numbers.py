class solution:
    def addTwoNumbers(self, l1, l2):
        curr1 = l1
        curr2 = l2

        l1 = 0
        l2 = 0

        while curr1!= None:
            l1 = l1*10 + curr1.val
            curr1 = curr1.next

        while curr2!= None:
            l1 = l1*10 + curr2.val
            curr2 = curr2.next

            sum = l1 + l2
            sum = str(sum)

            head = listNode(int(sum[0]))
            curr = head
            