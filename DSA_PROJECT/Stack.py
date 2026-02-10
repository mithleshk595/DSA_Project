stack = []

# Push 
stack.append("A")
stack.append("B")
stack.append("C")

print("Stack after pushing A, B, C:", stack)

# peek 
topElement = stack[-1]
print("peek: ", topElement)

#pop 
topElement = stack.pop()
print("pop: ", topElement)

#stack and pop 
print("Stack after pop: ", stack)

# isEmpty
isEmpty = not bool(stack)
print("isEmpty: ", isEmpty)

# Size
print("Size: ",len(stack))







