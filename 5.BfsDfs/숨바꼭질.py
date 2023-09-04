#1697
import sys
from collections import deque
n, y = map(int, sys.stdin.readline().split())

queue = deque([n])
visited = [0 for _ in range(1000001)]
while queue :
    x = queue.popleft()
    if x == y :
        print(visited[x])
        break
    for nx in (x-1, x+1, 2*x) : #모든 가능 루트
        if 0<= nx <=100000 and not visited[nx] : #방문했었으면 큐에 안넣음 -> 이미 그 루트로 진행중~ => 최적해 아님
            visited[nx] = visited[x] + 1
            queue.append(nx)