def longest_substring(string):
	arr = {}
	max_elem = 0
	j = 0
	for i in range(len(string)):
		if string[i] in arr:
			while j < i:
				arr[j] = False
				if string[j] == string[i]:
					j += 1
					break
				j += 1
		arr[string[i]] = True
		max_elem = max(max_elem, i - j + 1)
	return max_elem

if __name__ == '__main__':
	print longest_substring('pwwkew')
