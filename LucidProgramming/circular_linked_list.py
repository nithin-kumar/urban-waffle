class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None

class CircularLinkedList(Node):
	def __init__(self):
		self.head = None

	def append(self, data):
		if not self.head:
			self.head = Node(data)
			self.head.next = self.head
		else:
			curr = self.head
			while curr.next != self.head:
				curr = curr.next
			new_node = Node(data)
			curr.next = new_node
			new_node.next = self.head

	def preppend(self, data):
		new_node = Node(data)
		if not self.head:
			self.head = new_node
			self.head.next = self.head
		else:
			curr = self.head
			while curr.next != self.head:
				curr = curr.next
			new_node.next = self.head
			self.head = new_node
			curr.next = self.head

	def print_list(self):
		curr = self.head
		while curr.next != self.head:
			print curr.data
			curr  = curr.next
		if curr:
			print curr.data
		print '----------------'

	def remove(self, key):
		curr = self.head
		if not curr:
			return
		prev = None
		while curr and curr.data != key:
			prev = curr
			curr = curr.next
		if not curr:
			return
		if not prev:
			# Remove Head
			while curr.next != self.head:
				curr = curr.next
			# prev is the last node
			prev = curr
			curr_head = self.head
			self.head = curr_head.next
			prev.next = self.head
		else:
			prev.next = curr.next
			curr.next = None


clist = CircularLinkedList()
clist.append('A')
clist.append('B')
clist.append('C')
clist.append('D')
clist.append('E')
clist.print_list()
clist.remove('A')
clist.print_list()

			
		
		