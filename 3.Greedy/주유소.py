#13305
import sys
n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
p = list(map(int, sys.stdin.readline().split()))

cost = p[0]
result = 0

for i in range(n-1) :
    if cost > p[i] :
        cost = p[i]
    result += l[i]*cost

print(result)

'''
p[-1] = 10000000001

result = 0
midx = p.index(min(p))

for i in range(n-1):
    if max(p) == p[i] or p[i+1] < p[i] :
        result += l[i]*p[i]
        continue
    if min(p) == p[i] :
        result += p[i]*sum(l[i:])
        break
    result += l[i:midx]*p[i]
    for _ in range(i, midx) :
        p[i] = 0

print(result)
'''

