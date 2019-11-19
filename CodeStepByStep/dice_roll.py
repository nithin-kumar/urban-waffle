def diceRoll(n):
	diceRollHelper(n, [])

def diceRollHelper(n, path):
	if n == 0:
		print path
	else:
		for i in range(1, 7):
			path.append(str(i))
			diceRollHelper(n - 1, path)
			path.pop()

if __name__ == '__main__':
	diceRoll(2)