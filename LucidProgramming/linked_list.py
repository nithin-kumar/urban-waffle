class Node(object):
	"""docstring for Node"""
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList(object):
	"""docstring for LinkedList"""
	def __init__(self):
		self.head = None

	def print_list(self):
		current = self.head
		while current:
			print current.data
			current = current.next
		print '####################'

	def append(self, data):
		new_node = Node(data)
		if self.head == None:
			self.head = new_node
			return
		last_node = self.head
		while last_node.next:
			last_node = last_node.next
		last_node.next = new_node

	def preppend(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def insert_after_node(self, key, data):
		new_node = Node(data)
		current = self.head
		while current.data != key:
			current = current.next
		new_node.next = current.next
		current.next = new_node

	def delete_node(self, key):
		current = self.head
		if current.data == key:
			self.head = current.next
			current = None
			return
		prev = None
		while current and current.data != key:
			prev = current
			current = current.next
		if current:
			prev.next = current.next
			current = None
		return

	def delete_node_at_pos(self, pos):
		current = self.head
		if pos == 0:
			self.head = current.next
			current = None
			return
		prev = None
		count = 0
		while current and count != pos:
			prev = current
			count += 1
			current = current.next
		if current:
			prev.next = current.next
			current = None
		return

	def length_recursive(self, node):
		if not node:
			return 0
		return 1 + self.length_recursive(node.next)
	def length_iterative(self):
		count = 0
		current = self.head
		while current:
			count += 1
			current = current.next
		return count
	def swap_nodes(self, key_1, key_2):
		if key_1 == key_2:
			return
		prev_1 = None
		current_1 = self.head
		while current_1 and current_1.data != key_1:
			prev_1 = current_1
			current_1 = current_1.next

		prev_2 = None
		current_2 = self.head
		while current_2 and current_2.data != key_2:
			prev_2 = current_2
			current_2 = current_2.next

		if not current_1 or not current_2:
			return

		if prev_1:
			prev_1.next = current_2
		else:
			self.head = current_2
		if prev_2:
			prev_2.next = current_1
		else:
			self.head = current_1

		current_1.next, current_2.next = current_2.next, current_1.next

	def reverse_iterative(self):
		prev = None
		current = self.head
		while current:
			tmp = current.next
			current.next = prev
			prev = current
			current = tmp
		self.head = prev
		return
	
	def reverse_recursive(self):
		def reverse_recursive_helper(prev, current):
			if not current:
				return prev
			tmp = current.next
			current.next = prev
			prev = current
			current = tmp
			return reverse_recursive_helper(prev, current)
		self.head = reverse_recursive_helper(None, self.head)

	def merge_linked_list(self, l2):
		def merge_helper_recursive(s, p,q):
			if p is None:
				s.next = q
				return
			elif q is None:
				s.next = p
				return
			if p.data < q.data:
				s.next = p
				p = p.next
			else:
				s.next = q
				q = q.next
			s = s.next
			return merge_helper_recursive(s, p, q)
		def merge_helper_iterative(s, p, q):
			while p and q:
				if p.data < q.data:
					s.next = p
					p = p.next
				else:
					s.next = q
					q = q.next
				s = s.next
			if p is None:
				s.next = q
			elif q is None:
				s.next = p
			return
		p = self.head
		q = l2.head
		# Base Case
		if not p:
			return q
		if not q:
			return p
		
		if p.data < q.data:
			s = p
			p = p.next
		else:
			s = q
			q = q.next
		self.head = s
		#merge_helper_recursive(s, p, q)
		merge_helper_iterative(s, p, q)
		#return self.head

	def remove_duplicates(self):
		map_ = {}
		prev = None
		current = self.head
		while current:
			if current.data in map_:
				prev.next = current.next
				current = None
			else:
				prev = current
				map_[current.data] = True
			current = prev.next
		return self.print_list()

	def nth_from_last(self, n):
		# Method 1 - Length Method
		# length = self.length_iterative()
		# current = self.head
		# while length > n and current:
		# 	current = current.next
		# 	length -= 1
		# if not current:
		# 	return
		# return current.data
		# Method 2
		p = self.head
		q = self.head
		count = 0
		while q and count < n:
			q = q.next
			count += 1
		if not q and count == n:
			return p.data
		elif not q:
			return
		while p and q:
			p = p.next
			q = q.next
		return p.data 

	def rotate_list(self, k):
		# Method 1
		cur = self.head
		while cur and cur.data != k:
			cur = cur.next
		if not cur:
			return
		tmp = tmp2 = cur.next
		if tmp is None:
			return
		cur.next = None
		while tmp.next:
			tmp = tmp.next
		tmp.next = self.head
		self.head = tmp2

	def is_palindrom(self):
		if self.head is None:
			return True
		slow = self.head
		fast = self.head
		slow_prv = None
		while slow and fast and fast.next:
			slow_prv = slow
			slow = slow.next
			fast = fast.next.next
		if fast:
			# Linked List has Odd number of nodes
			# and the last node pointed by fast pointer
			# slow is the middle node
			# Reverse the first half nd check with next half
			p = slow.next
		else:
			p = slow
		slow_prv.next = None
		self.reverse_iterative()
		q = self.head
		while q and p:
			if q.data != p.data:
				return False
			p = p.next
			q = q.next
		return True

	def sum_two_lists_iterative(self, llist):
		p = self.head
		q = llist.head
		sum_list = LinkedList()
		sum_ = 0
		if p:
			sum_ += p.data
			p = p.next
		if q:
			sum_ += q.data
			q = q.next
		carry = sum_ / 10
		sum_list.head = Node(sum_ % 10)
		last_node = sum_list.head
		while p or q:
			sum_ = carry
			if p:
				sum_ += p.data
				p = p.next
			if q:
				sum_ += q.data
				q = q.next
			carry = sum_ / 10
			new_node =  Node(sum_ % 10)
			last_node.next = new_node
			last_node = new_node
		if carry != 0:
			new_node = Node(carry)
			last_node.next = new_node
		return sum_list.print_list()

	def sum_two_list_recursive(self, llist):
		def sum_two_list_recursive_helper(p, q, carry):
			if not p and not q and carry == 0:
				return
			sum_ = carry
			if p:
				sum_ += p.data
				p = p.next
			if q:
				sum_ += q.data
				q = q.next
			new_node = Node(sum_ % 10)
			carry = sum_ / 10
			new_node.next = sum_two_list_recursive_helper(p, q, carry)
			return new_node

		sum_ = 0
		p = self.head
		q = llist.head
		if p:
			sum_ += p.data
			p = p.next
		if q:
			sum_+= q.data
			q = q.next
		carry = sum_ / 10
		sum_list = LinkedList()
		sum_list.head = Node(sum_ % 10)
		current = sum_list.head
		current.next = sum_two_list_recursive_helper(p, q, carry)
		sum_list.print_list()




llist = LinkedList()
llist.append(5)
llist.append(6)
llist.append(3)
llist2 = LinkedList()
llist2.append(8)
llist2.append(4)
llist2.append(2)
llist.sum_two_lists_iterative(llist2)
llist.sum_two_list_recursive(llist2)



		