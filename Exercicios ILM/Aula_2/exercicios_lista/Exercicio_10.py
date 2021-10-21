# 10 - Calcule a nota final de um aluno sabendo que ela é composta da seguinte forma: Prova 1 (40%) +
#Prova 2 (40%) + Trabalhos (20%). Os três valores que compõem a nota final serão informados pelo
#usuário, exiba-a com duas casas decimais.

p1 = float (input ('Insira a nota da P1: '))
p2 = float (input ('Insira a nota da P2: '))
trab = float (input ('Insira a nota de Trabalhos: '))

notaFinal = (p1*0.4) + (p2*0.4) +(trab*0.2)

print('Nota final: %.2f'% notaFinal)
