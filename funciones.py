import array as ar

def create_mtx(n, m):
    A = []
    for i in range(n):
        for j in range(m):
            val = int(input('Ingresar el valor de A['+ repr(i) + ','+ repr(j)+ ']: '))
            if i == 0:
                A.append([val])
            else:
                A[j].append(val)
    return A

def null_mtx(n, m):
    A = []
    for i in range(n):
        for j in range(m):
            if i == 0:
                A.append([0])
            else:
                A[j].append(0)
    return A

def id_mtx(n, m):
    m = n
    A = []
    for i in range(n):
        for j in range(m):
            if i == 0:
                if i == j:
                    A.append([1])
                else:
                    A.append([0])
            else:
                if i == j:
                    A[j].append(1)
                else:
                    A[j].append(0)
    return A

def print_mtx(A):
    for j in range(0, len(A)):
        for i in range(0, len(A[0])):
            print(A[j][i], end='')
            if (i < len(A[0]) -1):
                print("    ", end='')
        print()

def is_empty(A):
    if A == []:
        return True
    else:
        return False
        
def prod(A, B):
    ca = len(A)
    fa = len(A[0])
    cb = len(B)
    fb = len(B[0])
    if ca == fb:
        res = null_mtx(fa, cb)
        for j in range(fa):
            for k in range(cb):
                sum = 0
                for i in range(ca):
                    sum = (A[i][j]*B[k][i]) + sum
                res[k][j] = sum
    else:
        print("Dimensiones incorrectas.")
    return res

def add(A, B):
    res = []
    if len(A) == len(B):
        if len(A[0]) == len(B[0]):
            c = len(A)
            f = len(A[0])
            for j in range(c):
                for i in range(f):
                    if i == 0:
                        res.append([A[j][i] + B[j][i]])
                    else:
                        res[j].append(A[j][i] + B[j][i])
    else:
        print("Dimensiones incorrectas.")
    return res

def sub(A, B):
    res = []
    if len(A) == len(B):
        if len(A[0]) == len(B[0]):
            c = len(A)
            f = len(A[0])
            for j in range(c):
                for i in range(f):
                    if i == 0:
                        res.append([A[j][i] - B[j][i]])
                    else:
                        res[j].append(A[j][i] - B[j][i])
    else:
        print("Dimensiones incorrectas.")
    return res

def traspose(A):
    res = []
    n = len(A[0])
    m = len(A)
    for i in range(n):
        for j in range(m):
            val = A[j][i]
            if j == 0:
                res.append([val])
            else:
                res[i].append(val)
    return res
# def inverse(A):
# def determinante(A):
# def diagonal(A):
# def LU(A):
# def valores_ppios(A):
# def vectores_ppios(A):
