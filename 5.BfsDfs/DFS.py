#DFS 메서드 정의
def DFS(graph, v, visited) :
    #현재 노드를 방문처리
    visited[v] = True
    print(v, end=' ')
    for i in graph[v] : #i도 결국에는 노드니까.. v와 인접한 노드
        if not visited[i] :
            DFS(graph, i, visited)
    
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

DFS(graph, 1, visited)
print()