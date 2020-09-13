# Python Program for factorial of a number
#
# Factorial of a non-negative integer, is multiplication of all integers smaller than or equal to n. For example factorial of 6 is 6*5*4*3*2*1 which is 720.

def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)

def factorial_iterative(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac


if __name__ == '__main__':
    i = int(input("enter the number for which factorial is needed :\t"))
    fact = factorial_recursive(i)
    print(fact)
    fac = factorial_iterative(i)
    print(fac)