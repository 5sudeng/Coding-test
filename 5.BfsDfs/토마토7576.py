#7576
from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

queue = deque()

for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 1 :
            queue.append((i, j))

dx = [-1, 1, 0, 0] #상 하 좌 우
dy = [0, 0, -1, 1]

while queue :
    x, y = queue.popleft()
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m or graph[nx][ny] == -1 :
            continue
        if graph[nx][ny] == 0 :
            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx, ny))

isBreak = False
for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 0 :
            isBreak = True

if isBreak :
    print(-1)
else :
    print(max(map(max, graph)) - 1)