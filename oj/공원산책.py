def solution(park, routes):
    dx = [-1, 1, 0, 0] #n s w e
    dy = [0, 0, -1, 1]
    dic = {"N":0, "E":3, "W":2, "S":1}
    n, m = len(park), len(park[0])
    for i in range(n) :
        isBr = False
        if "S" not in park[i] :
            continue
        for j in range(m) :
            if park[i][j] == 'S' :
                x, y = i, j
                isBr = True
                break
        if isBr :
            break
    
    for route in routes :
        dr, num = route.split()
        idx = dic.get(dr)
        nx, ny = x + dx[idx]*int(num), y + dy[idx]*int(num)
        
        if nx<0 or ny<0 or nx>=n or ny>=m :
            continue
        
        isCon = False
        
        for i in range(1, int(num)+1) :
            tx = x + i*dx[idx]
            ty = y + i*dy[idx]
            
            if park[tx][ty] == "X":
                isCon = True
                break
            
        if not isCon :
            x, y = nx, ny
        
    answer = [x, y]
    return answer