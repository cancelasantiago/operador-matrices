import funciones

r = funciones.Rational(2, 4)

arr = [['1/2','2'], ['1','2','4'], ['1']]
#print(funciones.print_mtx(funciones.init_mtx(0, 0, arr)))

# s = '1'
# print(funciones.from_str_to_rational(s).print_rational())

#funciones.print_mtx(funciones.init_mtx(arr))

funciones.print_mtx(funciones.inverse(funciones.init_mtx(arr)))