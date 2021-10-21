#6. Dado um número inteiro n (n > 1), exibir os números de n − 1 até 1. Quantos serão impressos?
n = int(input('Digite n: '))

contador = 0

while n > 1:
    n -= 1
    contador += 1

print(contador)
   
