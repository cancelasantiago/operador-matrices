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

# def matriz_vacia(A):
# def producto(A, B):
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
# def transpuesta(A):
# def inversa(A):
# def valores_ppios(A):
# def vectores_ppios(A):
