#11. Dados números inteiros, exibir a soma deles. A entrada termina com a leitura do número zero. Ao menos
#um número será lido antes do zero.

acumulador = 0
n = int(input('Digite n: '))

while True:

    while n > 0:
        n -= 0
        acumulador += n
        n = int(input('Digite n: '))    

    if n == 0:
        break

print(acumulador)
   
