#14. Dadas letras, uma por linha, exibir a quantidade de vogais lidas. A entrada é finalizada pelo caractere '!'.

contador = 0
vogais = 0
l = input('Digite a letra: ')

while l != '!':

    if l=='a'or l=='e' or l=='i' or l=='o' or l=='u':
        vogais += 1
    contador += 1
    l = input('Digite a letra: ')

print(vogais)
