#11. Dado um inteiro n, exibir o dia da semana correspondente (domingo = 1 e sábado = 7) ou 'dia inválido'.

n = int(input('Digite o número: '))

d1 = 'domingo'
d2 = 'segunda'
d3 = 'terça'
d4 = 'quarta'
d5 = 'quinta'
d6 = 'sexta'
d7 = 'sábado'

if 1 <= n <= 7:

    if n == 1:
       print(d1)
    if n == 2:
       print(d2)
    if n == 3:
       print(d3)
    if n == 4:
       print(d4)
    if n == 5:
       print(d5)
    if n == 6:
       print(d6)
    if n == 7:
       print(d7)
else:
       print('Dia inválida')
