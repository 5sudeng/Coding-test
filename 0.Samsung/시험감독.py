#13458
n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

result = 0

for i in a :
    tmp = (i - b) / c
    if tmp < 0 :
        result += 1
        continue
    if tmp > int(tmp) :
        result += 1
    result += int(tmp) + 1

print(int(result))