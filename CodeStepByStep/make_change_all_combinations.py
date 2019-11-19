def makeChange(amount, denominations):
	memo = {}
	result = makeChangeHelper(amount, denominations, memo)
	print result
# def makeChangeHelper(result, amount, denominations, chosen):
# 	# print 'makeChangeHelper(' + str(amount) + ',' + str(denominations) + ',' + str(chosen) + ')'
#  	if amount == 0:
# 		result.append(list(chosen))
# 		return
# 	elem = denominations[0]
# 	if amount - elem
# 	makeChangeHelper(result, amount - elem, denominations, chosen)

# 	chosen.append(elem)
# 	makeChangeHelper(result, amount - elem, denominations, chosen)

# 	chosen.pop()

# def makeChangeHelper(result, amount, denominations, chosen, i, current_sum):
# 	if i == len(denominations):
# 		result.append(list(chosen))
# 		return

# 	if current_sum + denominations[i] <= amount:
# 		chosen.append(denominations[i])
# 		makeChangeHelper(result, amount, denominations, chosen, i + 1, current_sum + denominations[i])
# 		chosen.pop()

def makeChangeHelper( amount, denominations, memo):
	key = str(amount) + '_' + '_'.join(map(str, denominations))
	if key in memo:
		return memo[key]
	print 'makeChangeHelper(' + str(amount) + ',' + str(denominations) + ')'
	count = 0
	if amount == 0:
		count = 1
	else:
		for i in range(len(denominations)):
			if amount - denominations[i] >=0:
				count += makeChangeHelper(amount - denominations[i], denominations[i:], memo)
	memo[key] = count
	return count

if __name__ == '__main__':
	makeChange(10, [1, 2, 3, 4, 5, 6])

