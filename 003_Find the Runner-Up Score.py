if __name__ == '__main__':
    n = int(input())
    arr = list(set(map(int, input().split())))
    print(arr)
    arr.sort()
    print(arr[-2])