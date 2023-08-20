n, m = map(int, input().split())
pos = [0, 0]
pos[0], pos[1], way = map(int, input().split())
maps = [list(map(int, input().split())) for i in range(m)]

dx = [1, 0, -1, 0] #북, 동, 남, 서 (0, 1, 2, 3)
dy = [0, 1, 0, -1] #북, 동, 남, 서 (0, 1, 2, 3)
d = [[0] * m for _ in range(n)] #방문 위치 저장

#왼쪽으로 회전
def turn_left() :
    global way
    way -= 1
    if way == -1 :
        way = 3

d[pos[0]][pos[1]] = 1
count = 1
turn_time = 0
while True :
    turn_left() 
    nx = pos[0] + dx[way]
    ny = pos[1] + dy[way]

    if d[nx][ny] == 0 and maps[nx][ny] == 0 : #회전 후 정면에 안가본 칸 있는 경우
        d[nx][ny] = 1
        pos[0], pos[1] = nx, ny
        count += 1
        turn_time = 0
        continue
    else : #나머지 경우 -> 가본 칸이거나 바다인 경우
        turn_time += 1
    if turn_time == 4 :
        nx = pos[0] - dx[way]
        ny = pos[1] - dy[way]
        
        if maps[nx][ny] == 0 :
            pos[0], pos[1] = nx, ny
        else : #뒤가 바다로 막혀있을 경우
            break
        turn_time = 0

print(count)
'''
count = 1
maps[pos[0]][pos[1]] = 1

while True :
    way = (way + 3)%4
    nx =  pos[0] + dx[way]
    ny = pos[1] + dy[way]
    if maps[nx][ny] != 1 :
        maps[nx][ny] = 1
        count += 1
        pos[0], pos[1] = nx, ny 
    if maps[pos[0]+1][pos[1]] + maps[pos[0]-1][pos[1]] + maps[pos[0]][pos[1]+1] + maps[pos[0]][pos[1]-1] == 4 :
        nx = pos[0] - dx[way]
        ny = pos[1] - dy[way]
        if nx == 0 or ny == 0 or nx == n-1 or ny == m-1 :
            break
        pos[0] , pos[1] = nx, ny

print(count)
'''

'''
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1 
'''