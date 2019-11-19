class Node(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class BinaryTree(object):
	def __init__(self, root):
		self.root = Node(root)

def isIdentical(root1, root2):
	# If both are None return True
	if not root1 and not root2:
		return True
	if root1 and root2:
		return root1.val == root2.val and isIdentical(root1.left, root2.left) and isIdentical(root1.right, root2.right)
	else:
		return False
