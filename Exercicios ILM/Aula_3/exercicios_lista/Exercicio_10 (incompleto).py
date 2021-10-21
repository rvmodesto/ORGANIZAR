#10. Fornecidas duas datas distintas, exibir qual delas ocorre primeiro. Cada data será fornecida em três
#valores inteiros, onde o primeiro representa o dia, o segundo o mês e o terceiro o ano.

from datetime import date

data_1 = int(input('Digite primeira data:'))
data_2 = int(input('Digite primeira data:'))

a = data_1.strftime('%d/%m/%y)
b = data_2.strftime('%d/%m/%y)

if data_1 > data_2:
    print(a)
else:
    print(b)
