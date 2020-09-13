A = [1,2,3]
B = [6,5,4]
C = [7,8,9]
X = [A] + [B] + [C]
print (list(zip(*X)))
print (list(zip(X[0],X[1],X[2])))