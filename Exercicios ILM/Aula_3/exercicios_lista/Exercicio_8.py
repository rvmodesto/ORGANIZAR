#8. Fornecidos os três segmentos de reta a, b e c (a > 0, b > 0 e c > 0), verificar se podem formar um
#triângulo. Exibir a mensagem 'formam' ou 'não formam', conforme o caso.

a = int(input('Digite o valor de a:'))
b = int(input('Digite o valor de b:'))
c = int(input('Digite o valor de c:'))

soma_1 = a + b
soma_2 = b + c
soma_3 = a + c

if c > soma_1:
    print('Formam')

elif a > soma_2:
    print('Formam')
    
elif b> soma_3:
    print('Formam')

else:
    print('Não formam')
