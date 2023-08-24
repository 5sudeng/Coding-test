#5585
mon = 1000 - int(input())
dong = [500, 100, 50, 10, 5, 1]

count = 0
for d in dong :
    if d > mon :
        continue
    count += mon//d
    mon %= d
    if mon == 0 :
        break

print(count)