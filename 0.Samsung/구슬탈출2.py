#13460 푸는 중..^^
from collections import deque

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]

dx = [-1, 1, 0, 0] #상 하 좌 우
dy = [0, 0, -1, 1]

red = deque()
blue = deque()
goal = []
for i in range(n) :
    for j in range(m) :
        if graph[i][j] == "R" :
            red.append((i, j))
        if graph[i][j] == "B" :
            blue.append((i, j))
        if graph[i][j] == "O" :
            goal.append((i, j))

count = 0
isBreak = False
befo = -5

while count < 10 and red and blue :
    x, y = red.popleft()
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m :
            continue
        if graph[nx][ny] == "O" :
            count += 1
            isBreak = True
            break
    if isBreak and graph[x-dx[i]][y-dy[i]] != "B" :
        break
    for i in range(4) :
        if befo + i in [1, 5]  :
            continue
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m :
            continue
        if graph[nx][ny] == "." :
            befo = i
            graph[nx][ny] = "R"
            graph[x][y] = "."
            while True :
                nx = nx + dx[i]
                ny = ny + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= m :
                    break #continue
                if graph[nx][ny] == "." :
                    graph[nx][ny] = "R"
                    graph[nx-dx[i]][ny-dy[i]] = "."
                elif graph[nx][ny] == "O" :
                    count += 1
                    isBreak = True
                    graph[nx][ny] = "R"
                    graph[nx-dx[i]][ny-dy[i]] = "O"
                    if graph[nx-2*dx[i]][ny-2*dy[i]] == "B" :
                        count = -1
                    break
                else :
                    red.append((nx-dx[i], ny-dy[i]))
                    count += 1
                    break
            x2, y2 = blue.popleft()
            nx2, ny2 = x2 + dx[i], y2 + dy[i]
            if nx2 < 0 or ny2 < 0 or nx2 >= n or ny2 >= m :
                continue
            if graph[nx2][ny2] == "#" :
                blue.append((x2, y2))
            if graph[nx2][ny2] == "." :
                graph[nx2][ny2] = "B"
                graph[x2][y2] = "."
                while True :
                    nx2 = nx2 + dx[i]
                    ny2 = ny2 + dy[i]
                    if nx2 < 0 or ny2 < 0 or nx2 >= n or ny2 >= m :
                        continue
                    if graph[nx2][ny2] == "." :
                        graph[nx2][ny2] = "B"
                        graph[nx2-dx[i]][ny2-dy[i]] = "."
                    elif graph[nx2][ny2] == "O" :
                        isBreak = True
                        count = -1
                        break
                    else :
                        blue.append((nx2-dx[i], ny2-dy[i]))
                        break
            break

    if isBreak :
        break

if count == 10 or count == 0 :
    count = -1
print(count)