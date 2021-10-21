#8. Dado um número inteiro n (n > 0), seguido de n números inteiros, exibir a soma dos n números lidos (o
#número n não entra na soma).
n = int(input('Digite n: '))

acumulador = 0

while n > 0:
    n -= 1
    acumulador += n

print(acumulador)
   
