def countBinary(n):
	countBinaryHelper(n, '')

def countBinaryHelper(n, prefix):
	if n == 0:
		print prefix
		return
	countBinaryHelper(n - 1, '0' + prefix)
	countBinaryHelper(n - 1, '1' + prefix)

if __name__ == '__main__':
	countBinary(3)

