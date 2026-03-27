# def fun1(i):
#     #Base Case

#     if i==5:
#         return
    
#     # Recursion Case
#     print(i, end="")
#     fun1(i+1)

#     fun1(0)


# def fun2(x,n):
#     #base case
#     if x==n:
#         # return
    
#     # recursion case
#     print(n, end=" ")
#     fun2(x, n-1)
# fun2(0,6)

# def fact(n):
#     #base case
#     if n==0 or n==1:
#         return 1
#     #recursive
#     return n*fact(n-1)
# print(fact(5))

# def gcd(a, b):
#     #base case
#     if b==0:
#         return 
#      #recursive case
#     return gcd(b, a%b)

# print(gcd(21, 70))
# print(gcd(56, 98))

def isPrime(n):
    if n==0 or n==1:
        return False
    for i in range(2, n):
        if n%i==0:
            return False
        return True
print(isPrime(11))
print(isPrime(15))
print(isPrime(2))
















