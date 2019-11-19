class BinarySearch(object):
	"""docstring for BinarySearch"""
	def __init__(self, arr):
		self.items = arr

	def search_iterative(self, key):
		if key is None:
			return -1
		low = 0
		high = len(self.items) - 1
		while low <= high:
			# mid = (low + high) / 2
			mid = low + (high - low)/2
			if self.items[mid] == key:
				return mid
			elif key < self.items[mid]:
				high = mid - 1
			else:
				low = mid + 1
		return -1

	def search_recursive(self, key, low, high):
		if low > high:
			return -1
		#mid = (low + high) / 2
		mid = low + (high - low)/2
		if self.items[mid] == key:
			return mid
		elif key < self.items[mid]:
			high = mid - 1
		else:
			low = mid + 1
		return self.search_recursive(key, low, high)

	def first_and_last(self, key):
		start = self.first_occurance_index(key)
		end = self.last_occurance_index(key)
		return (start, end)

	def first_occurance_index(self, key):
		# Iterative version
		start = 0
		end = len(self.items) - 1
		while start <= end:
			mid = start + (end - start)/2
			if self.items[mid] == key and (mid == 0 or self.items[mid-1] < key):
				return mid
			elif key <= self.items[mid]:
				end = mid - 1 
			else:
				start = mid + 1
		return -1

	def last_occurance_index(self, key):
		start = 0
		end = len(self.items) - 1
		while start <= end:
			mid = start + (end - start)/2
			if self.items[mid] == key and (mid == len(self.items) - 1 or self.items[mid + 1] > key):
				return mid
			elif key >= self.items[mid]:
				start = mid + 1
			else:
				end = mid - 1
		return -1 

	def index_of_least_element_greater_than_key(self, key):
		start = 0
		end = len(self.items) -1
		while start <= end:
			mid = start + (end - start)/2
			if self.items[mid] == key:
				if mid == len(self.items) - 1:
					return -1
				elif self.items[mid + 1] > key:
					return mid + 1
			if key >= self.items[mid]:
				start = mid + 1
			else:
				end = mid - 1
		return -1


	def index_of_greatest_element_less_than_key(self, key):
		start = 0
		end = len(self.items) -1
		while start <= end:
			mid = start + (end - start)/2
			if self.items[mid] == key:
				if mid == 0:
					return -1
				elif self.items[mid - 1] < key:
					return mid - 1
			if key <= self.items[mid]:
				end = mid - 1
			else:
				start = mid + 1
		return -1

	def rotation_point(self):
		# Method No Duplicates
		start = 0
		end = len(self.items) - 1
		while start <= end:
			mid = start + (end - start)/2
			if self.items[mid] > self.items[end]:
				start = mid + 1
			elif self.items[mid] < self.items[end]:
				end = mid - 1
			else:
				break
		return mid

		

bsearch = BinarySearch(['ptolemaic','retrograde', 'supplant',
                                     'undulate', 'xenoepist', 'asymptote',
                                     'babka', 'banoffee', 'engender',
                                     'karpatka', 'othellolagkage'])
#print bsearch.search_iterative(6)
#print bsearch.search_recursive(6, 0, len(bsearch.items) - 1)
#print bsearch.first_occurance_index(1)
#print bsearch.last_occurance_index(1)
#print bsearch.first_and_last(1)
#print bsearch.index_of_least_element_greater_than_key(11)
#print bsearch.index_of_greatest_element_less_than_key(21)
print bsearch.rotation_point()
