pos = input()

count = 0
x , y = pos[0], pos[1]

al = [i for i in "0abcdefg"]
x = al.index(x)
y = int(y)

dx = [2, 2, 1, 1, -2, -2, -1, -1]
dy = [1, -1, 2, -2, 1, -1, 2, -2]
n = len(dx)
for i in range(n) :
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n :
        continue
    count += 1

print(count)