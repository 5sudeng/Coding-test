#10773
import sys
k = int(sys.stdin.readline())
array = []
for i in range(k) :
    x = int(sys.stdin.readline())
    if x == 0 :
        array.pop()
        continue
    array.append(x)
    
print(sum(array))