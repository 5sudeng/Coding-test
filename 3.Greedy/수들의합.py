#1789
n = int(input())
count = 0

for i in range(1, n+1) :
    if n - i < i + 1 :
        count += 1 
        break
    n -= i
    count += 1

print(count)