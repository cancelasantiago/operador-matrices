import array as ar
from math import gcd

#Clase para trabajar con racionales

class Rational(object):
    def __init__(self, numerator, denominator):
        mcd = gcd(numerator, denominator)
        numerator = int(numerator/mcd) 
        denominator = int(denominator/mcd)
        
        if denominator == 0:
            raise Exception("El denominador no puede ser 0")
        else:
            self.numerator = numerator
            self.denominator = denominator

    def print_rational(self):
        if self.denominator == 1 or self.numerator == 0:
            if self.denominator == 0:
                return'0'
            else:
                return str(self.numerator)
        else: 
            return(str(self.numerator)+'/'+str(self.denominator))

    def set_rational(self, n,d):
        self.numerator = n
        self.denominator = d

    def get_numerator(self):
        return self.numerator
    
    def get_denominator(self):
        return self.denominator

def from_str_to_rational(s):
    if len(s) == 1:
        return Rational(int(s), 1)
    else: 
        return Rational(int(s.split('/')[0]), int(s.split('/')[1]))
    

#Suma racionales
def add_rational(a, b):
    numeratorA = a.getNumerator()
    denominatorA = a.getDenominator()
    numeratorB = b.getNumerator()
    denominatorB = b.getDenominator()
    if (denominatorB == denominatorA):
        numeratorR = numeratorA+numeratorB
        denominatorR = denominatorA
    else:
        k = gcd(denominatorA,denominatorB)
        numeratorR = k*(numeratorA+numeratorB)
        denominatorR = k*denominatorA
    res = Rational(numeratorR,denominatorR)
    return (0)

#Resta racionales
def sub_rational(a, b):
    numeratorA = int(a.getNumerator())
    denominatorA = int(a.getDenominator())
    numeratorB = int(b.getNumerator())
    denominatorB = int(b.getDenominator())
    return (0)

#Multiplicacion racionales
def mult_rational(a, b):
    numeratorA = int(a.getNumerator())
    denominatorA = int(a.getDenominator())
    numeratorB = int(b.getNumerator())
    denominatorB = int(b.getDenominator())
    return (0)

#Division racionales
def div_rational(a, b):
    numeratorA = int(a.getNumerator())
    denominatorA = int(a.getDenominator())
    numeratorB = int(b.getNumerator())
    denominatorB = int(b.getDenominator())
    return (0)

#Algoritmos simples
#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
def print_mtx(A):
    n = len(A)
    m = len(A[0])
    for j in range(m):
        for i in range(n):
            print(A[i][j].print_rational(), end='')
            if i != m-1:
                print(' '*(6-len(A[i][j].print_rational())), end='')
        print()
#-----------------------------------------------------------------------------------------------------
def init_mtx(arr):
    #arr[[1,2,3], [4,5,6], [7,8,9]]
    max = 0
    for a in arr:
        if max < len(a):
            max = len(a)
    for a in arr:
        dif = max - len (a)
        for i in range(dif):
            a.append('0')
    for a in arr:
        for j in range(len(a)):
            a[j] = from_str_to_rational(a[j])
    return arr
    # A = []
    # for i in range(n):
    #     for j in range(m):
            
    #         if i == 0:
    #             A.append([val])
    #         else:
    #             A[j].append(val)
    print(A)
    return A
#-----------------------------------------------------------------------------------------------------
def init_mtx_nula(n, m):
    A = []
    for i in range(n):
        for j in range(m):
            if i == 0:
                A.append([Rational(0, 1)])
            else:
                A[j].append(Rational(0, 1))
    #print(A)
    return A
#-----------------------------------------------------------------------------------------------------
def empty_mtx(A):
    if A == []:
        return True
    else:
        return False
#-----------------------------------------------------------------------------------------------------        
def prod(A, B):
    ca = len(A)
    fa = len(A[0])
    cb = len(B)
    fb = len(B[0])
    if ca == fb:
        res = init_mtx_nula(fa, cb)
        for j in range(fa):
            for k in range(cb):
                sum = 0
                for i in range(ca):
                    sum = add_rational(mult_rational(A[i][j]*B[k][i]) , sum)
                res[k][j] = sum
    else:
        print("Dimensiones incorrectas.")
    print(res)
    return res
#-----------------------------------------------------------------------------------------------------
def add(A, B):
    res = []
    if len(A) == len(B):
        if len(A[0]) == len(B[0]):
            c = len(A)
            f = len(A[0])
            for j in range(c):
                for i in range(f):
                    if i == 0:
                        res.append(add_rational([A[j][i] + B[j][i]]))
                    else:
                        res[j].append(add_rational(A[j][i] + B[j][i]))
    print(res)
    return res
#-----------------------------------------------------------------------------------------------------
def sub(A, B):
    res = []
    if len(A) == len(B):
        if len(A[0]) == len(B[0]):
            c = len(A)
            f = len(A[0])
            for j in range(c):
                for i in range(f):
                    if i == 0:
                        res.append(sub_rational([A[j][i] - B[j][i]]))
                    else:
                        res[j].append(sub_rational(A[j][i] - B[j][i]))
    print(res)
    return res
#-----------------------------------------------------------------------------------------------------
def transposed(A):
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
#-----------------------------------------------------------------------------------------------------
# def determinante(A):
#-----------------------------------------------------------------------------------------------------
def mtx_id(n):
    I = []
    for i in range(n):
                for j in range(n):
                    if (i == 0):
                        if (i == j):
                            I.append([Rational(1,1)])
                        else:
                            I.append([Rational(0, 1)])
                    else:
                        if (i == j):
                            I[j].append(Rational(1,1))
                        else:
                            I[j].append(Rational(0,1))
    return(I)
#-----------------------------------------------------------------------------------------------------
#Algoritmos 
#Algoritmo de Gauss Jordan para A^-1
def inverse(A):
    if (not empty_mtx(A)):
        n = len(A[0])
        m = len(A)
        if (n == m):
            I= mtx_id(n)
            for i in range (n):
                pivot = A[i][i]
                for k in range(n-1):
                    A[i][k] = div_rational(A[i][k], pivot)
                    I[i][k] = div_rational(I[i][k], pivot)
                for j in range(n-1):
                    if (i != j):
                        aux = A[j][i]
                        for k in range(n-1):
                            A[j][k] = sub_rational(A[j][k], mult_rational(aux, A[i][k]))
                            I[j][k] = sub_rational(I[j][k], mult_rational(aux, I[i][k]))
        else:
            print("La matriz no es cuadrada")
    else:
        print("La matriz es vacia")
    return A
#-----------------------------------------------------------------------------------------------------
# def canonical(A) 
# def mtx_asociada(A, T):
# def mtx_bases(A):
# def mtx_rep(T, A, B):
# def mtx_smj(A):
# def LU(A):
# def valores_ppios(A):
# def vectores_ppios(A):
# def sub_esp_ppios(A):
# def diagonal(A):
# def jordan_canonical_form(A)