#1193
x = int(input())
count1 = 0
result2 = 0

for i in range(x) :
    x -= i
    if x <= 0 :
        break
    count1 += 1
    result2 = x

result1 = count1 + 1 - result2
if count1 % 2 == 0 :
    print(f"{result2}/{result1}")
else :
    print(f"{result1}/{result2}")