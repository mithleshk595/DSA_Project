# set1 = {1, 2, 3, 4, 6, 8, 3, 2, 8}

# print(set1)


# set1 = {"hello", "world", 100, 100, 3.14, "hii"}
# print(set1)
# print(len(set1))

# set1 = {"hello", "world", 100, 100, 3.14, "hii"}

# set1.add("1")
# set1.add("100")
# set1.discard(100)

# print(set1)


set1 = {2, 3, 4, 5, 8, 9, 10}
set2 = {4, 6, 8, 10, 12 ,14}

# union 
print(set1 | set2)
print(set1.union(set2))

# intersection
print(set1 & set2)
print(set1.intersection(set2))

# diffrence
print(set1 - set2)
print(set1.difference(set2))


# diference 
print(set2 - set1)
print(set2.difference(set1))

# symmetric difference union - intersection
print(set1 ^ set2)
print(set1.symmetric_difference(set2))



