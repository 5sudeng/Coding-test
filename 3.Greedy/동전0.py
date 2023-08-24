#11047
import sys
n, k = map(int, sys.stdin.readline().split())
money = [int(sys.stdin.readline()) for _ in range(n)]

result = 0

for i in range(n-1, -1, -1) :
    cur = money[i]
    if cur > k :
        continue
    result += k // cur
    k %= cur
    if k == 0 :
        break

print(result)