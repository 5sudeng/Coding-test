n, m = map(int, input().split())

graph = [list(map(int, input())) for i in range(n)]

def dfs(x, y) : #약간 x가 노드..nth 줄.. y는 그노드에 딸린애
    if x <= -1 or y <= -1 or x >= n or y >= m :
        return False
    if graph[x][y] == 0 : #0인 곳 하나만 찾으면 주변거 다 1로 만들어둠 -> 중복 카운트 안되게 함
        graph[x][y] = 1
        dfs(x, y-1)
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(n) :
    for j in range(m) :
        if dfs(i, j) == True :
            result += 1

print(result)


'''
4 5
00110
00011
11111
00000
'''