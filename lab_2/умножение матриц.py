
#умножение матриц

A = []
B = []
for i in range(4):
    temp = []
    for j in range(4):
        temp.append(3)
    A.append(temp)
for i in range(4):
    temp = []
    for j in range(4):
        temp.append(3)
    B.append(temp)

print(A)
print(B)

def Matrix(a, b):
    D = []
    counter = 0
    for i in range(len(a[0])):
        temp = []
        for j in range(len(b)):
            temp.append(0)
        D.append(temp)
    print(D)
    if len(a) != len(b[0]):
        return
    else:
        for i in range(len(D)):
            for j in range(len(D[0])):
                for k in range(len(D)):
                    D[i][j] = a[i][k] * b[k][j]
                    counter = counter + D[i][j]
                D[i][j] = counter
                counter = 0
    return D
print(Matrix(A, B))





