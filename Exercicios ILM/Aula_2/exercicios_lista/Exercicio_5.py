#5- Fornecido um número inteiro n (1000 ≤ n ≤ 9999), exibir a soma dos dois dígitos à esquerda com os
#dois dígitos à direita. Exemplo: n = 3689, logo, a saída é 36 + 89 = 125.

numero = int(input('informe um número entre 1000 e 9999: '))

div_1 = numero // 1 % 100
div_2 = numero // 100 % 100

soma = div_1 + div_2

print('A soma é: ', soma)
