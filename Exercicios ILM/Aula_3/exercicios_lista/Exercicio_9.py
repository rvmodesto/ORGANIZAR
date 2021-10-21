#9. Fornecidos os três segmentos de reta a, b e c que formam um triangulo, exibir uma mensagem
#indicando qual o tipo de triangulo que será formado (equilátero, isósceles ou escaleno).


a = int(input('Digite o valor do lado a:'))
b = int(input('Digite o valor do lado b:'))
c = int(input('Digite o valor do lado c:'))

if a == b== c:
    print('Triângulo equilátero.')
elif a != b and b != c and a != c:
    print('Triângulo Escaleno')
else:
    print('Triângulo Escaleno')
