#скалярное умножение векторов

A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]

B = [5, 6, 8, 7, 9, 4, 3, 0, 1, 2, 3]

def Scalar(a, b):
    D = []
    if len(a) != len(b):
                return "Разную длину векторов"
    else:
        for i in range(len(a)):
            D.append(A[i] * B[i])
    return D
print(Scalar(A, B))

