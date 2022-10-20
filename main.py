from distutils.util import rfc822_escape
from math import gcd
import funciones

r1 = funciones.Rational(1, 2)
r2 = funciones.Rational(3, 2)
r3 = funciones.Rational(1, 3)
r4 = funciones.Rational(-1,1)


arr = [['1/2','2'], ['1','2','4'], ['1', '0', '1']]
arr_rational = funciones.init_mtx(arr)
print()
funciones.print_mtx(arr_rational)
print()
arr_inverse = funciones.inverse(arr_rational)
funciones.print_mtx(arr_inverse)

# s = '1'
# print(funciones.from_str_to_rational(s).print_rational())

#funciones.print_mtx(funciones.init_mtx(arr))