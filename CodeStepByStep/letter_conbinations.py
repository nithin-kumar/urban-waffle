def letterCombinations(nums):
	mapping = {'2' : ['a', 'b', 'c'], '3' : ['d', 'e', 'f'], '4' : ['g', 'h', 'i'], '5' : ['j', 'k','l'], '6' : ['m', 'n', 'o'],
				'7': ['p','q', 'r', 's'], '8' : ['t', 'u', 'v'], '9' : ['w', 'x', 'y', 'z'] }
	result = []
	letterCombinationsHelper(result, nums, mapping, '', 0)
	print result
def letterCombinationsHelper(result, nums, mapping, prefix, i):
	if len(nums) == i:
		result.append(prefix)
		return

	choices = mapping[nums[i]]
	for j in range(len(choices)):
		# Choose
		prefix += choices[j]

		# Explore
		letterCombinationsHelper(result, nums, mapping, prefix, i + 1)

		# Unchoose
		prefix = prefix[:-1]

if __name__ == '__main__':
	letterCombinations('236')