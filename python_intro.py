if 3 > 2: 
	print('it works!')

if 5 > 2:
	print('5 é maior que 2')
else:
	print('5 é menor que 2')

if 7 < 3:
	print('7 é menor que 3')
else:
	print ('7 é maior que 3')

name = 'Sofia'
if name == 'Thiago':
	print('Oi, Thiago')
elif name == 'Sofia':
	print('Olá, Sofia')
else:
	print('Olá, estranho')

name = 'Guilherme'
if name == 'Sofia':
	print('Olá, Sofia')
elif name == 'Thiago':
	print('Olá, Thiago')
else:
	print('Hello, stranger')

def hi():
	print('Bom diiiaaa')
	print('Como vai você nesse dia lindo?')
hi()

def hi2(name):
	print('hi ' + name + '!')
hi2("Clementine")	

girls = ['Valéria', 'Mônica', 'Fabiana', 'Elisa', 'Teresa']
for name in girls:
	hi2(name)

for i in range(1, 6):
	print(i)