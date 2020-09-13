# Given a number x, determine whether the given number is Armstrong number or not.
# A positive integer of n digits is called an Armstrong number of order n (order is number of digits) if.
#
# abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + ....

def isArmstrong(a):
    p = list(map(int, a))
    l = len(p)
    s = 0
    for i in p:
        s = s + (pow(int(i),l))
    return(s)

if __name__ == '__main__':
    n = input("Enter the number:\t")
    check = { True : "is armstrong", False : "is not armstrong" }
    s = isArmstrong(n)
    print(f"Number {n} is : {check[int(s) == int(n)]}")
