#2- Fornecido um número inteiro n (n ≥ 0), exibir o dígito mais à direita do valor, para tanto utilize o
#operador de resto (%).

numero = int(input('Informe um número ≥ 0: '))

div_1 = numero // 1 % 10

print('O digito mais a direita  de', numero, 'é: ', div_1)
