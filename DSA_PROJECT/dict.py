# dict1 = {}

# print(type(dict1))


# dict1 = {1: "Mithlesh", 2: "ashutosh", 3:"Mithlesh", 4: "Rahul"}

# print(dict1)
# print(len(dict1))
# print(type(dict1))


# dict1 = {1: "Mithlesh", 2: "ashutosh", 3:"Mithlesh", 4: "Rahul"}

# print(dict1)

# print(dict1[1])


# dict1[3] = "Yash"
# dict1[5] = "Yuvraj"

# dict1.pop(4)
# del dict1[2]

# print(dict1.update({6: "Ashish", 7: "Ram"}))


# print(dict1[3])
# print(dict1[5])


# print(dict1)


# dict1 = {1: "Mithlesh", 2: "Ashutosh", 3: "Swati", 4: "Rahul", 5: "Yuvraj", 6: "Ashish", 7: "Ram", 8: "Shivam", 9: "Monika", 10: "Rashi"}

# for i in dict1:
#     print(i, dict1[i])


# dict1 = {1: "Mithlesh", 2: "Ashutosh", 3: "Swati", 4: "Rahul", 5: "Yuvraj", 6: "Ashish", 7: "Ram", 8: "Shivam", 9: "Monika", 10: "Rashi"}

# for i in  dict1.keys():
#     print(i, dict1[i])

# print(list(dict1.keys()))


# dict1 = {1: "Mithlesh", 2: "Ashutosh", 3: "Swati", 4: "Rahul", 5: "Yuvraj", 6: "Ashish", 7: "Ram", 8: "Shivam", 9: "Monika", 10: "Rashi"}

# for i in  dict1.values():
#     print(i)

# print(list(dict1.values()))


# dict1 = {1: "Mithlesh", 2: "Ashutosh", 3: "Swati", 4: "Rahul", 5: "Yuvraj", 6: "Ashish", 7: "Ram", 8: "Shivam", 9: "Monika", 10: "Rashi"}

# for i, j in dict1.items():

#     print(i)

# print(list(dict1.items()))


list1 = [2, 3, 4, 5, 6, 9, 6, 5, ]

freq = {}

for i in list1:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
    

for i in freq:
    print(f"{i} is present {freq[i]} times?")


















