#2606
n = int(input())
m = int(input())
nodes = [list(map(int, input().split())) for i in range(m)]

graph = [[] for _ in range(n+1)]

result = -1

for i, j in nodes :
    graph[i].append(j)
    graph[j].append(i)

for i in range(n) :
    graph[i+1].sort()

visited = [False] * (n+1)

def dfs(v, visited) :
    visited[v] = True 
    global result
    result += 1
    for i in graph[v] :
        if not visited[i] :
            dfs(i, visited)
    return result
    

print(dfs(1, visited))
