def permuteDupe(arr):
	result = []
	map_ = {}
	permuteDupeHelper(result, arr, [], map_)
	return result

def permuteDupeHelper(result, arr, chosen, map_):
	print 'permuteHelper('+ str(chosen) + ',' + str(arr) + ')'
	if len(arr) == 0:
		print chosen
		#result.append(list(chosen))
		return
	for i in range(len(arr)):
		# Choose
		elem = arr[i]
		tmp = map(str, chosen + [elem])
		if '-'.join(tmp) not in map_:
			chosen.append(elem)
			del arr[i]

			# Explore
			permuteDupeHelper(result, arr, chosen, map_)

			# Unchoose
			chosen.pop()
			arr.insert(i, elem)
			map_['-'.join(tmp)] = 1
		


if __name__ == '__main__':
	arr = [1, 1, 2]
	#arr = [1, 2, 3]
	permuteDupe(arr)