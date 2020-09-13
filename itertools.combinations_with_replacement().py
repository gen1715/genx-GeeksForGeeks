from itertools import combinations_with_replacement
i,j = input().split()
# print(i,j)
for c in combinations_with_replacement(sorted(i), int(j)):
    print("".join(c))