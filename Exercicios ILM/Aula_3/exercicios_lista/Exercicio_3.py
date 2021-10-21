#3 - Fornecido um número n e um intervalo fechado de a até b (a < b), verificar se n está no intervalo.
# Exibir a mensagem 'no intervalo' ou 'fora do intervalo', conforme o caso.

n = int(input('Digite o valor de N: '))
a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))

if (a < n < b):
    print('no intervalo')
else:
   print('fora do intervalo')

