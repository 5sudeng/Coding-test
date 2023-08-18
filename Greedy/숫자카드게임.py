n, m = map(int, input().split())
cards = [list(map(int, input().split())) for i in range(n)]
small, idx = 0, 0

for rows in cards :
    if min(rows) > small :
        small = min(rows)
 
print(small)

'''
in
3 3
3 1 2
4 1 4
2 2 2

out
2
'''