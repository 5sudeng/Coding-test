N, M, K = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort(reverse=True)

first = nums[0]
second = nums[1]
 
'''
count = M
result = 0
for i in range(M) :
    if i % 2 == 0 :
        result += first * K
        count -= K
        if count < 0 :
            result += first * count
            break
    else :
        result += second
        count -= 1

print(result)
'''

count = (M//(K+1))*K
count += M%(K+1)

result = count * first
result += (M-count) * second

print(result)

'''
in
5 8 3
2 4 5 4 6

out
46
'''