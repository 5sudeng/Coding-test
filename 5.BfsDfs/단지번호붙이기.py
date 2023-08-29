#2667
n = int(input())
graph = [list(map(int, input())) for i in range(n)]

def dfs(x, y) :
    if x < 0 or y < 0 or x >= n or y >= n :
        return False
    if graph[x][y] == 1 : #방문 안했을 경우만 해야지 ㅠㅠ if 안하고 하니까 무한호출
        graph[x][y] = 0
        temp.append(1)
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)

count = 0
house = []
temp = []

for i in range(n) :
    for j in range(n) :
        if graph[i][j] == 0 :
            continue
        dfs(i, j)
        house.append(sum(temp))
        temp = []
        count += 1
        
house.sort()

print(count)
for i in house :
    print(i)