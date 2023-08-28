import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
nodes = [list(map(int, sys.stdin.readline().split())) for i in range(m)]

graph = [[] for i in range(n+1)]
for i, j in nodes :
    graph[i].append(j)
    graph[j].append(i)

for i in range(n+1) :
    graph[i].sort()

def dfs(graph, v, visited) :
    visited[v] = True
    print(v, end=' ')
    for i in graph[v] :
        if not visited[i] :
            dfs(graph, i, visited)

def bfs(graph, start, visited) :
    queue = deque([start])
    visited[start] = True
    while queue :
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True


dfs(graph, v, [False]*(n+1))
print()
bfs(graph, v, [False]*(n+1))