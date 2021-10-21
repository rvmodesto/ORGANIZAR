#2 - Fornecidos dois números inteiros a e b (a > 0 e b > 0), verificar se a é divisível por b. Exibir a
#mensagem 'divisível' ou 'não divisível', conforme o caso. Não use o operador de resto.

a = int (input('Digite o valor de A: '))
b = int (input('Digite o valor de B: '))

while a>= b:
    a-=b

if a==0:
    print('Divisível')

else:
    print('Não divisível')
