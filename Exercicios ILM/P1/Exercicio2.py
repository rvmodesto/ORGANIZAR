n = int(input('n? '))
soma = 0
while True:
    d = n%10
    n = n//10
    if d%2 == 1:
        soma = soma + d
    if n==0 :break
print('soma =', soma)
