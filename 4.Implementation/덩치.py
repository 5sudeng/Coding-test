#7586
n = int(input())

dungchi = [list(map(int, input().split())) for _ in range(n)]
results = [1 for _ in range(n)]

c1, c2 = 0, 0
for w1, h1 in dungchi :
    for w2, h2 in dungchi :
        if w1 < w2 and h1 < h2 :
            results[c1] += 1
        c2 += 1
    c2 = 0
    c1 += 1

for r in results :
    print(r, end=" ")