#12. Dados números reais, exibir a média aritmética deles. A entrada termina com a leitura do número zero.
x = float(input('Digite n: '))
acumulador = 0
contador = 0

while x != 0.0:
    acumulador += x
    contador += 1
    x = float(input('Digite n: '))

print('Média: %.2f' % (acumulador/contador))
   
