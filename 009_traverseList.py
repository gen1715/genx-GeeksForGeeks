tst = int(input("NUmber of test cases \n"))
lst = []
for i in range(tst):
    lst.append(int(input("Ënter the number for appenind into list \n")))

print(lst)

scorelist = []
lst2 = lst[:]
print(lst2)
for i in lst:
    score = 0
    for j in range(len(lst2)):
        if i > lst2[j]:
            score = score + 1
    scorelist.append(score)
print(scorelist)