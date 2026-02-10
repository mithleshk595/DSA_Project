queue = []

#Enqueue 
queue.append("A")
queue.append("B")
queue.append("C")
print("Queue", queue)

# peek 
frontElement = queue[0]
print("peek:", frontElement)

# Dequeue 
frontElement = queue.pop(0)
print("Dequeue:", frontElement)

# Queue after Dequeue
print("queue after Dequeue:", queue)

# isEmpty
isEmpty = not bool(queue)
print("isEmpty:", isEmpty)

# Size 
print("size:", len(queue))




