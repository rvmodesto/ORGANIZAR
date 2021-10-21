#12. Fornecidas as áreas de um círculo e de um quadrado, exibir 'esconde' se for possível ocultar
#completamente o quadrado sob o círculo, ou 'não esconde', caso contrário (adote π = 3,14).

c = float(input('Digite o valor área do circulo: '))
q = float(input('Digite o valor área do quadrado: '))

raio_c = float (c / 3.14)**0.5
lado_q = float (q)**0.5

d = raio_c*2

if d >= lado_q:
    print('Esconde')
else:
    print('Não esconde')
