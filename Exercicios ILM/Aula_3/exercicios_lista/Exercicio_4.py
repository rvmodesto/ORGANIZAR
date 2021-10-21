#4 - Fornecidos três números reais distintos a, b e c, exibir o maior valor. (seleção encadeada)

a = float (input('Digite o valor de A: '))
b = float (input('Digite o valor de B: '))
c = float (input('Digite o valor de C: '))

if a>b and a>c:
     print('O maior número é A')

elif  b>a and b>c:
       print('O maior valor é B')

else:
     print('O maior valor é C')
    
