
# An implementation of a iterative BFS with an adjacency list Time Complexity: O(V + E)
# @author Nithin Kumar, kv.nithin.90@gmail.com
from collections import defaultdict

class UndirectedGraph(object):
	def __init__(self):
		self.graph = defaultdict(list)

	def addUndirectedEdge(self, from_, to):
		self.graph[from_].append(to)

	def bfs(self, start, end, n):
		prev = self.solve(start, n)
		print prev
		return self.reconstructPath(start, end, prev)

	def solve(self, start, n):
		visited = [False]  * n
		prev = [False] * n
		queue = [start]
		while len(queue) != 0:
			node = queue.pop(0)
			visited[node] = True
			for neighbour in self.graph[node]:
				if not visited[neighbour]:
					queue.append(neighbour)
					prev[neighbour] = node
		return prev

	def reconstructPath(self, start, end, prev):
		path = [end]
		parent = prev[end]
		while parent:
			path.append(parent)
			parent = prev[parent]
		path.reverse()
		if path[0] == start:
			return path
		return []

	def count_nodes(self, start, n):
		queue = [start]
		DEPTH_TOKEN = -1
		queue.append(DEPTH_TOKEN)
		count = 0
		visited = [False] * n
		while len(queue) != 0:
			node = queue.pop(0)
			# If we encounter a depth token this means that we
      		# have finished the current frontier and are about
      		# to start the new layer (some of which may already
      		# be in the queue) or have reached the end.
			if node == DEPTH_TOKEN:
				# No more nodes to process
				if len(queue) == 0:
					break
				else:
					# Add another DEPTH_TOKEN
					queue.append(DEPTH_TOKEN)
			else:
				count += 1
				for neighbour in self.graph[node]:
					if not visited[neighbour]:
						visited[neighbour] = True
						queue.append(neighbour)
		return count



graph = UndirectedGraph()
graph.addUndirectedEdge(1, 2)
graph.addUndirectedEdge(1, 3)
graph.addUndirectedEdge(2, 4)
graph.addUndirectedEdge(1, 4)
graph.addUndirectedEdge(4, 5)
graph.addUndirectedEdge(3, 4)

# print graph.bfs(1, 5, 6)
print graph.count_nodes(1,6)

'''
1---- 2
|\    |
|  \  |
3    \ 4
'''
		