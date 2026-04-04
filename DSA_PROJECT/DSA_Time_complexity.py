# n = 10
# x = 3
# for i in range(n):
#     if i == x:
#         break
#     print(i, end=" ")

# 0(n)

# n = 0

# for i in range(n/2):
#     print(i, end = " ")


# for i in range(n/100):
#     print(i, end= " ")


# for i in range(n+100):
#     print(i, end= " ")


# for i in range(n*100):
#     print(i, end= " ")

# n = 10
# m = 100
# for i in range(n+m):
#     print(i, end= " ")




# for i in range(n):
#     print(i, end=" ")

# for i in range(n**2):
#     print(i, end=" ")

# for i in range(n):
#     for j in range(n):
#         print(i, j, end= " ")


# n = 100

# while n > 0:
#     print(n, end= " ")
#     n = n//2


# n = 1

# while n < 100:
#     print(n, end= " ")
#     n*=2


# i = 1
# n = 100

# while i <= n:
#     print(i, end= " ")
#     i*=2


# n = 5
# i = 1

# while i<= n:
#     print(i, end= " ")
#     i+=1

# def fact(n):
#     if n == 0:
#         return 1
#     return n*fact(n-1)


# print(fact(4))


def fun(n):
    if n == 0:
        return
    fun(n-1)

    print(n, end=" ")

    fun(3)
    