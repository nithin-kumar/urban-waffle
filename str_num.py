def str_to_num(string):
	result  = 0
	for i in range(len(string)):
		result +=  10 ** i * int(string[len(string) - i -1])
	print result

if __name__ == '__main__':
	str_to_num("66")