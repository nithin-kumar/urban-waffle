
def spiral_array(inputMatrix):
	right = True
	bottom = False
	left = False
	top = False
	left_limit = 0
	right_limit = len(inputMatrix[0]) - 1
	bottom_limit = len(inputMatrix) - 1
	top_limit = 0
	row = 0
	out = []
	col = len(inputMatrix[0]) - 1
	while left_limit <=  right_limit and top_limit <= bottom_limit:
		if right:
			for i in range(left_limit, right_limit + 1):
				print inputMatrix[row][i],
				#out.append(inputMatrix[row][i])
			row += 1
			top_limit +=1
			right = False
			bottom = True
		elif bottom:
			for i in range(top_limit, bottom_limit + 1):
				print inputMatrix[i][col],
			col -= 1
			right_limit -= 1
			bottom = False
			left = True
		elif left:
			for i in range(right_limit, left_limit - 1, -1):
				print inputMatrix[bottom_limit][i],
			bottom_limit -= 1
			left = False
			top = True
		elif top:
			for i in range(bottom_limit, top_limit - 1, -1):
				print inputMatrix[i][left_limit],
			left_limit += 1
			top = False
			right = True
	return out

if __name__ == '__main__':
	inputMatrix  = [ [1, 2,   3,  4,    5],
                   [6,    7,   8,  9,   10],
                   [11,  12,  13,  14,  15],
                   [16,  17,  18,  19,  20] ]
	spiral_array(inputMatrix)