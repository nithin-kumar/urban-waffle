def max_sum(arr, limit):
	result = max_sum_helper(arr, limit, 0)
	print result
def max_sum_helper(arr, limit, current_sum):
	if len(arr) == 0:
		if current_sum != 0:
			return current_sum
		return 0
	if current_sum > limit:
		return 0
	elem = arr[0]
	del arr[0]
	excluding_current_elem = max_sum_helper(arr, limit, current_sum)
	including_current_elem = 0
	if current_sum + elem <= limit:
		current_sum += elem
		including_current_elem = max_sum_helper(arr, limit, current_sum)
		current_sum -= elem
	arr.insert(0, elem)
	out = max(excluding_current_elem, including_current_elem)
	return out


if __name__ == '__main__':
	max_sum([6, 2, 6, 9, 1], 30)