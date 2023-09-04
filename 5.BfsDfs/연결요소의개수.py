#11724
import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
nodes = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for i, j in nodes :
    graph[i].append(j)
    graph[j].append(i)

def bfs(start) :
    queue = deque([start])
    visited[start] = True
    while queue :
        x = queue.popleft()
        for v in graph[x] :
            if not visited[v] :
                visited[v] = True
                queue.append(v)

count = 0

while True :
    if False in visited[1:] :
        v = visited[1:].index(False)+1
    else :
        break
    bfs(v)
    count += 1
print(count)