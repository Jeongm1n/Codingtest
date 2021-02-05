def solution(array, commands):
    answer = []
    for element in commands:
        temp = array[element[0]-1:element[1]]
        temp.sort()
        answer.append(temp[element[2]-1])
    return answer
array = list(map(int, input().split()))
commands = [list(map(int, input().split())) for _ in range(3)]
print(solution(array, commands))