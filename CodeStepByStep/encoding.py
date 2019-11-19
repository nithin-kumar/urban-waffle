def encoding(string, n):
	normalized = string.upper()
	out = ''
	for i in normalized:
		if i == ' ':
			out += ' '
		else:
			out += chr(ord('A') + ((ord(i) - ord('A')) + n ) % 26)
	return out

if __name__ == '__main__':
	print encoding('DWWDFN CHUJ DW GDZQ', -3)