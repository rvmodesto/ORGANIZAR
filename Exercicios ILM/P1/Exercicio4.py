L = int(input('Linhas? '))
C = int(input('Colunas'))

for l in range (1, L+1):
    for c in range (1,C+1):
         print('(%d,%d)' % (l, c), end=' ')
print()

