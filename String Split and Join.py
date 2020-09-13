def stringSpliter(n):
    a = '-'.join(n.split(" "))
    return a


if __name__ == '__main__':
    print("Please input a string :")
    n = input()
    output = stringSpliter(n)
    print(output)
