#16. Dado um número inteiro n (n > 0), seguido de n números inteiros, exibir o menor número lido.
n = int(input('Digite o número:'))

quantidade = 0
maior = 0
menor = 0

while True:

    while n != 0:
    quantidade += 1
    continuar = input('coninuar:')
        if continuar == 'S':
            n = int(input('Digite o número:'))
        if quantidade == 1:
            maior = menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
        elif continuar == 'N':  
        print('Menor valor digitado:', menor)
    else:
    print('Opção inválida')

