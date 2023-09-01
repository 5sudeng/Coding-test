#7576
import sys

m, n = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(day, x, y) : 
    if graph[x][y] == day or graph[x][y] == -1 :
        return
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=m or graph[nx][ny] != 0 :
            continue
        graph[nx][ny] = day

def isAlone(x, y) :
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=m :
            continue
        if graph[nx][ny] != -1 :
            return False
    return True

isBreak = False 

for i in range(n*m) : 
    j, k = i//m , i%m
    if graph[j][k] != 0 :
        continue
    if isAlone(j, k) :
        isBreak = True
        break

day = 2
while not isBreak :
    temp = 0
    for i in range(n*m) :
        j, k = i//m , i%m
        value = graph[j][k]
        if value == 0 :
            temp += 1
            continue
        if value != 0 or value != -1 or value != day:
            bfs(day, j, k)
    
    day += 1

    if temp == 0:
        break

print(day - 3)