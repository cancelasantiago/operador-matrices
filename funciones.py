import array as ar

def inicializar_matriz():
    n = int(input('Ingresar la cantidad de filas: '))
    m = int(input('Ingresar la cantidad de columnas: '))


    A = []
    for i in range(n):
        for j in range(m):
            val = int(input('Ingresar el valor de A['+ repr(i) + ','+ repr(j)+ ']: '))
            if i == 0:
                A.append([val])
            else:
                A[j].append(val)
    print(A)
    return A

def inicializar_matriz_nula(n, m):
    A = []
    for i in range(n):
        for j in range(m):
            if i == 0:
                A.append([0])
            else:
                A[j].append(0)
    #print(A)
    return A


"""def print_mtx(A):
    c = len(A)
    f = len(A[0])
    for j in range(c):
        for i in range(f):"""

def matriz_vacia(A):
    if A == []:
        return True
    else:
        return False
        
def producto(A, B):
    ca = len(A)
    fa = len(A[0])
    cb = len(B)
    fb = len(B[0])
    if ca == fb:
        res = inicializar_matriz_nula(fa, cb)
        for j in range(fa):
            for k in range(cb):
                sum = 0
                for i in range(ca):
                    sum = (A[i][j]*B[k][i]) + sum
                res[k][j] = sum
    else:
        print("Dimensiones incorrectas.")
    print(res)
    return res

def suma(A, B):
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
    print(res)
    return res

def resta(A, B):
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
    print(res)
    return res

def transpuesta(A):
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
    #print(res)
    return res
# def inversa(A):
# def determinante(A):
# def diagonal(A):
# def LU(A):
# def valores_ppios(A):
# def vectores_ppios(A):
