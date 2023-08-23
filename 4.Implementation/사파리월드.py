n = int(input())
m = int(input())

#n, m = map(int, input().split())

'''
if n < m :
    print(m - n)
else : # n >= m
    print(n - m)
'''

result = n - m
if result < 0 : #음수일 때
    print(-result)
else : #0이하일 때
    print(result)