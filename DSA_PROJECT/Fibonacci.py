# class Solution:
#     def fib(self, n: int) -> int:

#         #base case
#         if n==0 or n==1:
#             return n

#         #Recursive case
#         return self.fib(n-1) + self.fib(n+2)


# def gcd(a, b):
#     if b == 0:
#         return a 
#     return gcd(b, a % b)

# def lcm(a, b):
#     return (a  * b) // gcd(a, b)

# print(gcd(12, 15))
# print(lcm(12, 15)


# names = ["Alice", "bob", "Charcle", "dave"]

# names[0]= "Abhinav"

# print(type(names))
# print(names[0])
# print(names[-1])


# list1 = [1, 2, 3, 4, 5, 6]

# list1.append(7)
# list1.append(89)
# list1.append([1,2,3])
# list1.extend([1, 2, 3])

# print(list1)

list1 = [32, 45, 67, 89, 23, 12]

# list1.insert(2, 100)
# list1.insert(0, 200)

# list1.sort()

# print(list1)


# list1 = [32, 34, 45, 33, 44, 56, 57]

# list1.remove(44)
# list1.pop(1)

# print(list1)


# list1 = [32, 34, 45, 33, 44, 56, 57]

# print(min(list1))
# print(max(list1))


# list1 = [1, 2, 3, 4, 5, 5, 5, 6, 7, 6, 1, 2,]

# print(list1.count(4))
# print(list1.count(1))


# list1.sort()
# print(list1)

# list1.reverse()
# print(list1)


# list1 = [3, 4, 5, 6, 5, 7]

# print(list1.index(5))
# print(list1.index(5, 3))


# list1 = [2, 3, 4, 5]
# list2 = list1.copy() # shallow copy


# list2.append(6)
# print(list1, id(list1))
# print(list2, id(list2))


# list1 = [23, 45, 57, 89, 12, 34, 56]

# print(list1[2:5])  
# print(list1[:4])
# print(list1[3:])
# print(list1[:])


list1 = [23, 45, 57, 89, 12, 34, 56]

print(list1[::-1])






