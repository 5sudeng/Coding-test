#7569 
from collections import deque
import sys

m, n, H = map(int, sys.stdin.readline().split())
graph = [[list(map(int, sys.stdin.readline().split())) for i in range(n)] for j in range(H)]

#호출 순서 -> h 선택, n 선택, m 선택

#익어있는 토마토의 위치 저장
queue = deque()
for i in range(H) :
    for j in range(n) :
        for k in range(m) :
            if graph[i][j][k] == 1 :
                queue.append((i, j, k))

#상하좌우위아래 
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]

while queue :
    h, x, y= queue.popleft()
    for i in range(6) :
        nx = x + dx[i]
        ny = y + dy[i]
        nh = h + dh[i]
        if nx<0 or ny<0 or nh<0 or nx>=n or ny>=m or nh>=H :
            continue
        if graph[nh][nx][ny] == -1 :
            continue
        if graph[nh][nx][ny] == 0 :
            graph[nh][nx][ny] = graph[h][x][y] + 1
            queue.append((nh, nx, ny))

isBreak = False
result = 0
for i in range(H) :
    for j in range(n) :
        for k in range(m) :
            temp = graph[i][j][k]
            if temp == 0 :
                isBreak = True
                break
            if temp > result :
                result = temp
        if isBreak :
            break
    if isBreak :
        break

if isBreak :
    print(-1)
else :
    print(result - 1)
