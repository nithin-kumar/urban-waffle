# An implementation of a 2D Dungeon problem using BFS
# @author Nithin Kumar, kv.nithin.90@gmail.com

class Solution:
	def solve(self, m, start_row, start_col):
		def explore_neighbours(r, c, nodes_in_next_layer):
			# Direction Vectors for N, E, S, W
			dr = [-1, +1, 0, 0]
			dc = [0, 0, -1, +1]
			for i in range(4):
				rr = r + dr[i]
				cc = c + dc[i]
				if rr >= 0 and rr < rows and cc >= 0 and cc < columns:
					if not visited[rr][cc] and m[rr][cc] != '#':
						visited[rr][cc] = True
						prev[rr][cc] = (r, c)
						nodes_in_next_layer += 1
						rqueue.append(rr)
						cqueue.append(cc)
			return nodes_in_next_layer

		
		rows = len(m)
		columns = len(m[0])
		rqueue = [start_row]
		cqueue = [start_col]
		visited = [[False for i in range(columns)] for j in range(rows)]
		prev = [[False for i in range(columns)] for j in range(rows)]
		exit_reached = False
		exit_cordinate = 0
		nodes_in_current_layer = 1
		nodes_in_next_layer = 0
		step_count = 0
		while len(rqueue) != 0:
			r = rqueue.pop(0)
			c = cqueue.pop(0)
			visited[r][c] = True
			if m[r][c] == 'E':
				exit_cordinate = (r, c)
				exit_reached = True
				break
			nodes_in_next_layer = explore_neighbours(r, c, nodes_in_next_layer)
			nodes_in_current_layer -= 1
			if nodes_in_current_layer == 0:
				step_count += 1
				nodes_in_current_layer = nodes_in_next_layer
				nodes_in_next_layer = 0
		if exit_reached:
			x = exit_cordinate[0]
			y = exit_cordinate[1]
			path = [(x, y)]
			while (x, y) != (start_row, start_col):
				val = prev[x][y]
				path.append((val[0], val[1]))
				x = val[0]
				y = val[1]
			return step_count, path[::-1]
		return -1

sol = Solution()
m = [['S', '.', '#', '#'],
	 ['.', '.', '.', '#'],
	 ['.', '#', '.', '#'],
	 ['.', '.', '.', 'E'],
	 ['.', '.', '.', '.']]
print sol.solve(m, 0, 0)
