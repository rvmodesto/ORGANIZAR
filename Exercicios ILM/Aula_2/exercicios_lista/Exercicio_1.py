preço = int(input('Digite o preço: '))
quantidade = int(input('Digite a quantidade de peças: '))

total = int((preço * quantidade) - ((preço * quantidade)*0.1))
print('valor total: ', total)
