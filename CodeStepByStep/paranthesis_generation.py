def paranthesisGenerater(n):
	result = set()
	paranthesisGeneraterHelper(result, n, '')
	print list(result)

def paranthesisGeneraterHelper(result, n, prefix):
	#print 'paranthesisGeneraterHelper(' + str(n) + ',' + prefix + ')'
	if n == 0:
		#print prefix
		result.add(prefix)
		return
	paranthesisGeneraterHelper(result, n - 1, prefix + '()')
	paranthesisGeneraterHelper(result, n - 1, '()' + prefix )
	paranthesisGeneraterHelper(result, n - 1,  '('+ prefix + ')' )

if __name__ == '__main__':
	paranthesisGenerater(1)