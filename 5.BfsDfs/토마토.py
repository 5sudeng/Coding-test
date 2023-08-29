#7576
import sys

m, n = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

visited = [[-1 for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(day, x, y) : 
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=m or graph[nx][ny] != 0 :
            continue
        graph[nx][ny] = 1
        visited[nx][ny] = day

def isAlone(x, y) :
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=m :
            continue
        if graph[nx][ny] != -1 :
            return False
    return True

result = 0

isBreak = False 

for i in range(n) :
    for j in range(m) :
        isBreak = isAlone(i, j)
        if isBreak :
            break
    if isBreak :
        result = -1
        break

while not isBreak :
    temp = 0
    isBreak = False
    for i in range(n) :
        for j in range(m) :
            if visited[i][j] == result :
                continue
            if graph[i][j] == 0 :
                temp += 1
                continue
            if graph[i][j] == 1 :
                bfs(result, i, j)
    
    if temp == 0:
        break
    result += 1

print(result)