# n! = n*(n-1)*(n-2)...3*2*1
# e.g. 3! = 3*2*1


def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    return fact


print(factorial(31))
