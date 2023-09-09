def solution(name, yearning, photo):
    answer = []
    for p in photo :
        temp = 0
        for each in p :
            if each not in name :
                continue
            temp += yearning[name.index(each)]
        answer.append(temp)
    return answer