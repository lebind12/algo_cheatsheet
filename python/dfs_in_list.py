import sys
from collections import deque

n, m, r = map(int, sys.stdin.readline().split(' '))
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
stack = deque()
queue = deque()

# dfs
stack.append(r)
while True:
	if len(stack) == 0:
		break
	v = stack.pop()
	if visited[v] != 0:
		continue
	else:
		visited[v] = 1
		for vertex in graph[v]:
			if visited[vertex] == 0:
				stack.append(vertex)