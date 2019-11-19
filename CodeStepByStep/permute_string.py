def permuteString(string):
	result = set()
	permuteStringHelper(result, list(string), '')
	print result

def permuteStringHelper(result, list_, prefix):
	print 'permuteStringHelper(' + str(list_) + ',' + prefix + ')'
	if len(list_) == 0:
		print prefix
		result.add(prefix)
		return
	for i in range(len(list_)):
		# choose
		prefix += list_[i]
		char = list_[i]

		del list_[i]

		# Explore
		permuteStringHelper(result, list_, prefix)
		# Unchoose
		prefix = prefix[:-1]
		list_.insert(i, char)

if __name__ == '__main__':
	permuteString("abca")

