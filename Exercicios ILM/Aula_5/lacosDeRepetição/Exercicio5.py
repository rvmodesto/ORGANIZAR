#5. Dado um número inteiro n (n > 1), exibir os números de n − 1 até 0. Quantos serão impressos?
#nessa condição, quantas vezes você anotará o n -=1

n = int(input('Digite n: '))

contador = 0

while n > 0:
    n -= 1
    contador += 1

print(contador)
