#9. Dado um número inteiro n (n > 0), seguido de n números inteiros, exibir a soma dos n números lidos
#cujos valores sejam pares.

acumulador = 0
n = int(input('Digite n: '))

while n > 0:
    n -= 2
    acumulador += n

print(acumulador)
   
