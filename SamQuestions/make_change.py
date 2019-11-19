def make_chage(denominations, limit, memo, i):
	if limit in memo:
		print 'Hit' , limit
		return memo[limit]
	print 'make_chage(' + str(denominations) + ',' + str(limit)+')'
	# Selecting the base case
	# 1) Deleting item from arr and checking the len == 0
	# 2) Subtracting the limit and checking for limit == 0
	if limit == 0:
		# what should i return here, parameter like chosen? 
		return 0
	# should i iterate using index or directly using item?
	min_coins = 999999999
	for i in range(len(denominations)):
		if limit - denominations[i] >=0:
			min_coins = min(min_coins, make_chage(denominations, limit - denominations[i], memo, i))
	memo[limit] = min_coins + 1
	return min_coins + 1


memo = {0 : 0}
print make_chage([357,239,73,52],9832, {}, 0)