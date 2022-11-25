import sys
from collections import deque


# bfs 방문 표시는 pop이 아닌 append에 해주어야 중복 append를 방지할 수 있다.
n, m, r = map(int, sys.stdin.readline().split(' '))
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
stack = deque()
queue = deque()

# bfs
queue.append(r)
while True:
	if len(queue) == 0:
		break
	v = queue.leftpop()
	if visited[v] != 0:
		continue
	else:
		visited[v] = 1
		for vertex in graph[v]:
			if visited[vertex] == 0:
				queue.append(vertex)
	