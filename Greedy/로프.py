#2217
import sys
n = int(sys.stdin.readline())
m = [int(sys.stdin.readline()) for i in range(n)]

m.sort(reverse=True)

temp = 0
for i in range(n) :
    new = (i+1)*m[i]
    if new > temp :
        temp = new

print(temp)