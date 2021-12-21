import array as ar

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
