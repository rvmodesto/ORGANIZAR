#13. Dadas letras, uma por linha, exibir a quantidade de letras lidas. A entrada é finalizada pelo caractere '!'.
contador = 0

l = input('Digite a letra:')

while l != '!':
    contador += 1
    l = input('Digite a letra:')

print(contador)
