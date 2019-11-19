from datetime import datetime
from datetime import timedelta 

class IdStore(object):
	def __init__(self):
		self.id = 0

	def get_id(self):
		self.id += 1
		return self.id

class ReviewPattern(object):
	@classmethod
	def fib(self, n):
		if n == 0 or n == 1:
			return n
		a = 1
		b = 2
		for i in range(3, n + 1):
			c = a + b
			a = b
			b = c
		return b

class ReviewTopic(ReviewPattern):
	"""docstring for ReviewTopic"""
	def __init__(self, topic, id_store, date, desc=''):
		self.id = id_store.get_id()
		self.topic = topic
		self.description = desc
		self.created = datetime.strptime(date, '%Y-%m-%d')
		self.review_count = 0
		self.last_review_date = datetime.strptime(date, '%Y-%m-%d')
		self.next_review_date = self.next_date()
		
	
	def review_topic(self, date):
		self.review_count += 1
		self.last_review_date = datetime.strptime(date, '%Y-%m-%d')
		self.next_review_date = self.next_date(datetime.strptime(date, '%Y-%m-%d'))

	def next_date(self, date=datetime.now()):
		days = ReviewPattern.fib(self.review_count)
		next_review_date = self.last_review_date + timedelta(days=days)
		if next_review_date.date() < date.date():
			return date.date()
		return next_review_date.date()



class ReviewBook(ReviewPattern):
	"""docstring for ReviewBook"""
	def __init__(self):
		self.items = []

	def add(self, review_topic):
		self.items.append(review_topic)

	def mark_as_reviewed(self, topic_ids):
		for topic in topic_ids:
			for item in self.items:
				if item.id == topic[0]:
					item.review_topic(topic[1])
		return True

	def get_review_list(self, date=datetime.now()):
		items = self.items
		out = []
		for item in items:
			next_review_date = item.next_review_date
			if next_review_date == date.date() or next_review_date < date.date():
				out.append(item)

		return out


def main():
	print '\n\n#############  The Review Book #############\n'
	topics_to_review = [
		['Linked List Swap Nodes', '2019-09-27', 'LucidProgramming'],
		['Linked List Reversal', '2019-09-28', 'LucidProgramming'],
		['Merge Linked List(Recursive and Iterative)', '2019-10-05', 'https://www.youtube.com/watch?v=6ui3pEgOT70&list=PL5tcWHG-UPH112e7AN7C-fwDVPVrt0wpV&index=11'],
		['Remove Duplicates in Linked List', '2019-10-05', 'LucidProgramming'],
		['Singly Linked Lists -- Nth-to-Last Node', '2019-10-06', 'LucidProgramming'],
		['Singly Linked Lists -- Count Occurances', '2019-10-06', 'LucidProgramming'],
		['Singly Linked Lists -- Rotate List', '2019-10-06', 'LucidProgramming'],
		['Binary Search and its Modifications', '2019-10-07', 'GeekForGeek'],
	]

	# Add the reviewd topic ID here
	reviewed_topics = [[1, '2019-10-03'],
					   [2, '2019-10-03'],
					   [1, '2019-10-05'],
					   [2, '2019-10-05'],
					   [3, '2019-10-05'],
					   [4, '2019-10-05']
	]
	book = ReviewBook()
	id_store = IdStore()
	
	for i in topics_to_review:
		new_topic = ReviewTopic(i[0], id_store, i[1], i[2])
		book.add(new_topic)
	"""
	i = 0
	while i < 20:
		items = book.items
		#for item in items:
		print items[0].topic, items[0].next_review_date, items[0].review_count, ReviewPattern.fib(items[0].review_count)
		items[0].review_topic()
		i +=1
	return
	"""
	book.mark_as_reviewed(reviewed_topics)
	today = datetime.now() + timedelta(days=0)
	review_items = book.get_review_list(today)
	if len(review_items) == 0:
		print "No Topics to review for today. Enjoy!\n"
	else:
		print "\nTopics to review today\n"
		print "Topic ID               Topic Name              Description         Next Review Date"
		print "--------               ----------              -----------         ----------------"
		for item in review_items:
			if item.next_review_date < today.date():
				next_date = str(today.date())
			else:
				next_date = str(item.next_review_date)
			print str(item.id) + " " * 10 + item.topic + " "*10 + item.description + " " * 10 + next_date +  "\n"

	print "Add the topic ids to the reviewed_topics array to mark it as reviewed. Thanks\n"
if __name__ == '__main__':
	main()
		



		
		