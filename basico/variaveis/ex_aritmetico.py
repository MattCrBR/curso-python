# O exercicio consiste no preenchimento das variáveis, no calculo do IMC e o uso de f-strings
nome = 'Matheus Cravo'
altura = 1.70
peso = 64
imc = peso / (altura*altura)
print(nome, 'tem', altura, 'de altura')
print('pesa', peso, 'quilos e seu imc e:', imc)

linha_1 = f'{nome} tem {altura: .2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc e: {imc:.2f}'
print(linha_1)
print(linha_2)
