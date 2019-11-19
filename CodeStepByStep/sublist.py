def sublist(arr):
	result = []
	sublistHelper(result, 0, arr, [])
	#print result

def sublistHelper(result, i, arr, path):
	#print 'sublistHelper', result, i, arr, path
	if len(arr) == 0:
		print path
		result.append(list(path))
		return

	#pathWithCurrent = list(path)
	#pathWithCurrent.append(arr[i])
	#sublistHelper(result, i + 1, arr, path)
	#sublistHelper(result, i + 1, arr, pathWithCurrent)
	elem = arr[0]
	arr.pop(0)

	sublistHelper(result, i, arr, path)
	path.append(elem)
	sublistHelper(result, i, arr, path)

	path.pop()
	arr.insert(0, elem)

if __name__ == '__main__':
	sublist(['Jane', 'Bob', 'Matt', 'Sara'])