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

# def producto(A, B):
# def suma(A, B):
# def resta(A, B):
# def inversa(A):
# def valores_ppios(A):
# def vectores_ppios(A):
