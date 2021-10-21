#4. Dado um número inteiro n (com quatro dígitos), exibir o dígito mais à esquerda do valor.

numero = int(input('informe um número entre 1000 e 9999: '))

div = numero // 1000 % 10



print('O digito mais a esquerda de', numero, 'é: ', div)
