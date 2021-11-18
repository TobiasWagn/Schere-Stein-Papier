import random

def intToMove(i):
	if i==1:
		return 'Schere'
	elif i==2:
		return 'Stein'
	elif i==3:
		return 'Papier'
	
def Computer():
	i=random.randint(1,3)
	return i
	
def richtig(a, b):
	if (a==b):
		return('Unentschieden')
	elif (a=='Schere') and b==('Papier'):
		return('Du hast verloren')
	elif (a=='Papier') and b==('Schere'):
		return('Du hast gewonnen')
	elif (a=='Schere') and b==('Stein'):
		return('Du hast gewonnen')	
	elif (a=='Stein') and b==('Papier'):
		return('Du hast gewonnen')
	elif (a=='Papier') and b==('Stein'):
		return('Du hast verloren')	
	elif (a=='Stein') and b==('Schere'):
		return('Du hast verloren')
	elif (a=='Schere') and b==('Stein'):
		return('Du hast verloren')
	

if __name__ == '__main__':	
	print('Lust auf eine Runder Schere/Stein/Papier? [1,2,3]')
	print('"Schnick ... Schnack ... Schnuck" ')

	moveNumbPlayer = input()
	moveNumbComp = Computer()
	movePlayer = intToMove(int(moveNumbPlayer))
	moveComp = intToMove(moveNumbComp)

	print('Du wählst: '+movePlayer)
	print('Der Computer wählt: '+moveComp)
	print('----------------')
	print(richtig(movePlayer, moveComp))
	print('----------------')

