#6 - Dado um salário atual em reais e uma idade em anos, calcular o novo salário, que será o salário atual
#acrescido da idade em porcentagem. Exemplo: salário atual = R$ 1000,00 e idade = 23, logo,
#novo salário = R$ 1000,00 + 23% de R$ 1000,00 = R$ 1230,00. Exiba apenas o novo salário.


salario = float(input('Entre com o Salário Atual: '))
idade = int (input('Insira sua idade: '))

novoSalario = float (salario + (salario * (idade/100)))

print('Novo salário = ', novoSalario)
