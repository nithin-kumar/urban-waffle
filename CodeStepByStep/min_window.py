def min_window(s, t):
	max_ = len(s)
	result = max_
	min_ = len(t)
	source_map = {}
	target_map = {}
	window = ''
	if len(t) > len(s):
		return window
	for i in range(min_):
		target_map[ord(t[i])] = target_map.get(ord(t[i]), 0) + 1
		if ord(s[i]) in target_map:
			source_map[ord(s[i])] = source_map.get(ord(s[i]), 0) + 1
	if target_map == source_map:
		return t
	i = 0
	j = min_
	while j - i < result:
		if ord(s[j]) in target_map:
			source_map[ord(s[j])] = source_map.get(ord(s[j]), 0) + 1
		if source_map == target_map:
			if j - i + 1 <= result:
				window = s[i:j+ 1]
				result = min(result, j - i + 1)
				print 'Found j', s[i:j+ 1], result, j - i + 1, min_
		while j - i + 1 > min_:
			if ord(s[i]) in target_map:
				source_map[ord(s[i])] = source_map.get(ord(s[i]), 0) - 1
			i += 1
			if source_map == target_map:
				result = min(result, j - i + 1 )
				print 'Found i', s[i:j+1], result, j - i + 1
				window = s[i:j+1]
		print i, j, result
		j += 1
	return window

if __name__ == '__main__':
	#print min_window("abc", "b")
	# print min_window("abc", "ac")
	print min_window("ADOBECODEBAN", "ABC")