# # a= input()
# # print(f"input given by you is {a}")
# # b = a.split()
# # print(f"after a.split() {b}")
#
# # creating a set
# my_set = {1,2,3,1,1,2}
# print(my_set)
#
# my_set1 = set('a')
# print(my_set1)
# my_set2 = my_set1.add('b')
# print(my_set2)
# my_set2

if __name__ == '__main__':

    i,M = int(input("Number of elements in sets \n")), set(input("elements in sets \n").split())
    j,N = int(input("Number of elements in sets \n")), set(input("elements in sets \n").split())
    print(M)
    print(N)
    a = M.difference(N)
    b = N.difference(M)
    print('\n'.join(a.union(b)))


