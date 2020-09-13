def factorial_iterative(n):
    fac = 1
    for i in range(n):
        fac =  fac * (i+1)
    return fac

def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)



number = int(input("Ënter the number : \n"))
print("Factorial using iterative method", factorial_iterative(number))
print("Factorial using recursive method", factorial_recursive(number))

