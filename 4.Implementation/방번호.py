#1475
rnum = input()
array = [0 for _ in range(10)]

for num in rnum :
    array[int(num)] += 1

count1 = (array[6] + array[9] + 1)//2
count2 = max(array[:6]+array[7:9])

print(max(count1, count2))