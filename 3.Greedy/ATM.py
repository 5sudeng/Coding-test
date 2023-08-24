#11399
import sys
n = int(sys.stdin.readline())
time = list(map(int, sys.stdin.readline().split()))

time.sort()
result = 0

for i, t in enumerate(time) :
    result += t*(n-i)

print(result)