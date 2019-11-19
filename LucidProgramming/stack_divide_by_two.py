from stack import Stack

def integer_to_binary(num):
	s = Stack()
	while num != 0:
		reminder = num % 2
		num //= 2
		s.push(reminder)

	out = ''
	while not s.is_empty():
		out += str(s.pop())

	return out

if __name__ == '__main__':
	print integer_to_binary(0)
