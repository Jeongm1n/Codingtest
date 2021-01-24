def solution(priorities, location):
    answer=0
    m=max(priorities)
    while 1:
        idx = priorities.pop(0)
        if m==idx:
            answer += 1
            if location == 0:
                break
            else:
                location -= 1
            m = max(priorities)
        else:
            priorities.append(idx)
            if location == 0:
                location = len(priorities)-1
            else:
                location -= 1
    return answer
    
priorities = [2, 1, 3, 2]
location = 2
print(solution(priorities, location))