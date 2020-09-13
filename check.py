def fac(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return(fac)

if __name__ == '__main__':
    n = int(input())
    fac = fac(n)
    print(fac)

