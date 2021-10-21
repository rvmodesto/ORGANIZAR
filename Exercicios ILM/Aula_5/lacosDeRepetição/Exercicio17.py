#17. Dados dois números inteiros p (p ≥ 0) e q (q > 0), exibir a divisão inteira de p por q sem usar os
#operadores de divisão, multiplicação e/ou potência.
a = int(input('a: '))
b = int(input('b: '))
q = 0

while a >= b:
    a -= b
    q += 1

print('Divisão:', q)

