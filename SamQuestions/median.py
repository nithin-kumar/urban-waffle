def median_arrays(arr1, arr2):
	return (median(arr1) + median(arr2)) / 2.0

def median(arr):
	if len(arr) % 2 == 0:
		return (arr[(len(arr)/ 2) - 1] + arr[len(arr)/ 2]) / 2
	else:
		return arr[(len(arr) / 2)]

if __name__ == '__main__':
	print median_arrays([1, 3, 5], [2, 4, 6])