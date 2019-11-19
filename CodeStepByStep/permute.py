def permute(arr):
	result = []
	permuteHelper(result, arr, [])
	return result

def permuteHelper(result, arr, chosen):
	print 'permuteHelper('+ str(chosen) + ',' + str(arr) + ')'
	if len(arr) == 0:
		print chosen
		#result.append(list(chosen))
		return
	for i in range(len(arr)):
		# Choose
		elem = arr[i]
		chosen.append(elem)
		del arr[i]

		# Explore
		permuteHelper(result, arr, chosen)

		# Unchoose
		chosen.pop()
		arr.insert(i, elem)
		

if __name__ == '__main__':
	arr = [1, 1, 2]
	#arr = [1, 2, 3]
	permute(arr)