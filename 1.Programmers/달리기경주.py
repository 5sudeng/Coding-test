def solution(players, callings):
    count = dict()
    for i, player in enumerate(players) :
        count[player] = i
    
    for calling in callings :
        id = count.get(calling)
        front = players[id-1] #front player
        
        count[calling] -= 1
        count[front] += 1
        
        players[id-1], players[id] = calling, front
        
    return players