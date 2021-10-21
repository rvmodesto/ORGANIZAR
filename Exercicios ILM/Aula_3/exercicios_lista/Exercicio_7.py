#7. Fornecidos os coeficientes de uma equação de segundo grau (com a ≠ 0, ou seja, não é necessário
#verificar a existência da equação), exibir suas raízes.
#Obs.: Caso Δ seja negativo, imprimir as raízes no formato x − yi e x + yi, após calcular x e y.

import math

a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))

delta = float((b**2) - 4*a*c)

if delta == 0:
    y1 = (-b + math.sqrt(delta)) / (2*a)
    print('a raiz desta equação é: ', y1)

elif delta < 0:
    print('esta equação não possui raizes reais')

else:
    y1 = (-b + math.sqrt(delta))/(2*a)
    y2 = (-b + math.sqrt(delta))/(2*a)
    raizes = [y1,y2]
    raizes.sort()
    print('as raizes da equação são', raizes)
    
