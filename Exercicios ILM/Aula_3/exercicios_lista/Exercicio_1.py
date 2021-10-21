#1 - Observe as seguintes características:
#
#O número 2025 tem: 20 + 25 = 45 e 45 × 45 = 2025
#O número 1063 tem: 10 + 63 = 73 e 73 × 73 ≠ 1063
#
#Dado um número inteiro positivo n de quatro dígitos, verificar se n é um número cuja raiz quadrada é
#formada pela soma de suas dezenas. Exibir 'sim' ou 'não'. Não use o operador de potência, nem funções.

numero = int(input('Digite um número inteiro com 4 digitos: '))

div_1 = numero // 1 % 100
div_2 = numero // 100 % 100

soma = div_1 + div_2

raiz = soma * soma

if raiz == numero:
    print('sim')

else:
    print('não')


