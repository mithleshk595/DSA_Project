# class solution:
#     def lenthOfLastWord(self, s: str) -> int:
#         s = s.strip()
#         n = len(s)

#         i = -1
#         while i >=(-1*n) and s[i]!= " ":
#             i-=1
        
#         i+=1
#         return n - i


# set1 =  {2, 4, "Hello", 2, 3, "mithlesh", 4, 5, "Hello"}

# print(set1)
# print(len(set1))
# print(type(set1))


# list1 = [2, 4, 32, 54, 55, 32, 55, 67, 54, 32]

# # count number of unique elements in list1

# set1 = set(list1)
# print(len(set1))




set1 = {2, 4, "Hello", 2, 3, "mithlesh"}

set1.add("Hello")
set1.add("world")

set1.discard("Hello")
set1.discard("2")


# print(set1)


set1 = {2, 4, 6, 8, 10, 12}
set2 = {1, 2, 3, 4, 5, 6, 7}

# uninon
print(set1 | set2)
print(set1.union(set2))

# intersection 
print(set1&set2)
print(set1.intersection(set2))

# diffrence
print(set1-set2)
print(set1.difference(set2))

# diffrence
# print(set2-set1)
# print(set2.difference(set))

# symmetric diffrence
print(set1^set2)
print(set1.symmetric_difference(set2))

























