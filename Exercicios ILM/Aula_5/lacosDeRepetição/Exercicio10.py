#10. Dados números inteiros, exibir a soma deles. A entrada termina com a leitura do número zero.
n = int(input('Digite n: '))
acumulador = 0

while n != 0:
    acumulador += n
    n = int(input('Digite n: '))

print(acumulador)
   
