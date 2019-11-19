
# An implementation of a iterative DFS with an adjacency list Time Complexity: O(V + E)
# @author Nithin Kumar, kv.nithin.90@gmail.com
from collections import defaultdict

class Edge(object):
	"""docstring for Edge"""
	def __init__(self, from_, to, cost):
		self._from = from_
		self.to = to
		self.cost = cost

class DirectedGraph(object):
	"""docstring for Graph"""
	def __init__(self):
		self.graph = defaultdict(list)
	def addDirectedEdge(self, from_, to, cost):
		self.graph[from_].append(Edge(from_, to, cost))

	# Perform a depth first search on a graph with n nodes
	# from a starting point to count the number of nodes
	# in a given component.
	def DfsAdjacencyListIterative(self, start, n):
		count = 0
		visited = [False] * n
		stack = [start]
		while len(stack) != 0:
			node = stack.pop()
			visited[node] = True
			count += 1
			neighbours = self.graph[node]
			for neighbour in neighbours:
				if not visited[neighbour.to]:
					stack.append(neighbour.to)
		return count

	# Perform a depth first search on a graph with n nodes
	# from a starting point to count the number of nodes
	# in a given component.
	def DfsAdjacencyListRcursive(self, start, n):
		def DfsAdjacencyListRcursiveHelper(visited, node):
			if visited[node]:
				return 0

			# Visit the node
			visited[node] = True
			count = 1
			for neighbour in self.graph[node]:
				# Recursive find all reachable nodes
				count += DfsAdjacencyListRcursiveHelper(visited, neighbour.to)
			return count
		visited = [False] * n
		return DfsAdjacencyListRcursiveHelper(visited, start)


g = DirectedGraph()
g.addDirectedEdge(0, 1, 4)
g.addDirectedEdge(0, 2, 5)
g.addDirectedEdge(1, 2, -2)
g.addDirectedEdge(1, 3, 6)
g.addDirectedEdge(2, 3, 1)
print g.DfsAdjacencyListIterative(3, 5)
print g.DfsAdjacencyListRcursive(3, 5)
