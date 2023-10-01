#13460
from collections import deque

n, m = map(int, input().split())
graph = [input() for _ in range(n)]

dx = [-1, 1, 0, 0] #상 하 좌 우
dy = [0, 0, -1, 1]

red = deque()
blue = deque()
for i in range(n) :
    for j in range(m) :
        if graph[i][j] == "R" :
            red.append((i, j))
        if graph[i][j] == "B" :
            blue.append((i, j))

