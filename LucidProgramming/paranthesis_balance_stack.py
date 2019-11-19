from stack import Stack

def is_balanced(expression):
	stack = Stack()
	for item in expression:
		if item in ['(', '[', '{']:
			stack.push(item)
		else:
			if is_matching_paranthesis(stack.peek(), item):
				stack.pop()
			else:
				return False
	if not stack.is_empty():
		return False
	return True


def is_matching_paranthesis(p1, p2):
	if p1 == '(' and p2 == ')':
		return True
	elif p1 == '[' and p2 == ']':
		return True
	elif p1 == '{' and p2 == '}':
		return True
	return False

if __name__ == '__main__':
	print is_balanced("()[]{{(())}")


