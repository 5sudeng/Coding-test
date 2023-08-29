n, m = map(int,input().split())

graph = [list(map(int, input())) for i in range(n)]

#dfs로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y) : #약간 x가 노드..nth 줄.. y는 그노드에 딸린애
    #주어진 범위를 벗어나는 경우 즉시 종료
    if x <= -1 or y <= -1 or x >= n or y >=m :
        return False
    if graph[x][y] == 0 : #방문 안했으면 방문처리 -> #0인 곳 하나만 찾으면 주변거 다 1로 만들어둠 -> 중복 카운트 안되게 함
        graph[x][y] = 1
        #상 하 좌 우 모두 재귀적 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

#모든 노드에 대하여 음료수 채우기
result = 0
for i in range(n) :
    for j in range(m) :
        #현재 위치에서 DFS 수행
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