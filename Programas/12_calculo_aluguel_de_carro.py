dias = int(input('Quantos dias alugado?'))
km = float(input('Quantos km rodados?'))
pagar = (dias * 60) + (km * 0.15)
print('O valor total a pagar é de R$ {:.2f}'.format(pagar))
