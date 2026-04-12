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
