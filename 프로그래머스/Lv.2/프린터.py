def solution(priorities, location):
    idx = [i for i in range(len(priorities))]
    length = len(priorities)
    value = priorities[location]
    answer = 0
    while 1:
        temp = priorities.pop(0)
        temp_idx = idx.pop(0)
        if len(priorities) == 0:
            return length
        if temp < max(priorities):
            priorities.append(temp)
            idx.append(temp_idx)
        else:
            answer += 1
            if temp == value and temp_idx == location:
                return answer
priorities = list(map(int, input().split()))
location = int(input())
print(solution(priorities, location))