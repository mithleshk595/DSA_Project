def fact(n):
    #base case
    if n==0 or n==1:
        return 1
    #recursive
    return n*fact(n-1)
print(fact(5))

def gcd(a, b):
    #base case
    if b==0:
        return 
     #recursive case
    return gcd(b, a%b)

print(gcd(21, 70))
print(gcd(56, 98))
