x  = int(input('x? '))
qtd = 0
for i in range (1, x+1):
    if x % i == 0:
        print (i , end= ' ')
        qtd += 1
print('\nQuantidade = ', qtd)
