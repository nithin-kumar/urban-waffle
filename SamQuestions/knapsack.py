def knapsack(items, max_weight):
	def knapsack_helper(items, max_weight, c_w, c_v, max_value):
		print 'knapsack_helper(' + str(items) + ',' + str(c_w) + ',' + str(c_v)+ ')'
		if len(items) == 0:
			max_value = max(max_value, c_v)
			return max_value
		elem = items[0]
		del items[0]
		excluding_current_elem = knapsack_helper(items, max_weight, c_w, c_v, max_value)
		including_current_elem = 0
		if elem[0] + c_w <= max_weight:
			including_current_elem = knapsack_helper(items, max_weight,
													 c_w + elem[0],
													 c_v + elem[1],
													 max_value)
		items.insert(0, elem)
		out = max(excluding_current_elem, including_current_elem)
		return out
	return knapsack_helper(items, max_weight, 0, 0, 0)

if __name__ == '__main__':
	print knapsack([(1, 6), (2, 10), (3, 12)], 5)

