def findAnagrams(s, p):
	out = []
	map_ = [0]* 256
	for j in p:
		map_[ord(i) - ord('a')] += 1
	for i in range(len(s)):
		j = i
		tmp = ord(s[j]) - ord('a')
		if map_[tmp] != 0:
			while j - i < len(p):
				if if map_[tmp] != 0:
					break
				j += 1
			print s[i:j]
			if j - i == len(p):
				out.append(i)
	return out

if __name__ == '__main__':
	print findAnagrams('cbaebabacd', 'abc')