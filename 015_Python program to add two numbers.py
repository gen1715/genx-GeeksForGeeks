# Input: num1 = 5, num2 = 3
# Output: 8
#
# Input: num1 = 13, num2 = 6
# Output: 19

def add_num(x,y):
    return(x+y)

if __name__ == '__main__':
    i,j = int(input("Enter first number\t")), int(input("Enter second number\t"))
    res = add_num(i,j)
    print(f"sum of number is :", res)
