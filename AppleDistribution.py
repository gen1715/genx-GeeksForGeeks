def appleDistribution():
    print("Please provide number of apples : ")
    n = int(input())
    print (f"Number of apple provided to harry is {n}")
    print("Please provide number of students : ")
    mn = int(input())
    print (f"Number of students harry has {mn}")
    print("Please provide maximum number apple to distribute : ")
    mx = int(input())
    print (f"Number of apple to distribute by harry is {mx}")

    for i in range(mn,mx+1) :
        if n % i == 0 :
            print(f"for {i} Number is divisible")
        else :
            print(f"for {i} Number is not divisible")


appleDistribution()

