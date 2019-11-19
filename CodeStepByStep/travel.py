def travel(x, y):
	travel_helper(0, 0, x, y, [])

def is_bound(p, q, x, y):
	if p > x or q > y:
		return False
	return True
def travel_helper(p, q, x, y, path):
	#print 'travel_helper(' + str(p) + ',' + str(q) + ',' + str(x) +',' + str(y) + ',' + str(path) + ')'
	if p == x and q == y:
		print path
		return True
	if not is_bound(p, q, x, y):
		return False
	
	# choose
	path.append('E')
	result1 = travel_helper(p + 1, q, x, y, path)
	path.pop()
	path.append('N')
	result2 = travel_helper(p, q + 1, x, y, path)
	path.pop()
	path.append('NE')
	result3 = travel_helper(p + 1, q + 1, x, y, path)
	path.pop()
if __name__ == '__main__':
	travel(2, 2)


