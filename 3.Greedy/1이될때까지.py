n, k = map(int, input().split())
count = 0 
 
while True :
    if n % k == 0 :
        n //= k
    else :
        n -= 1
    count += 1
    if n == 1 :
        print(count)
        break

'''
in
17 4
out 
3
'''