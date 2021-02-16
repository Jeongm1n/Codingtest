def solution(s):
    temp = s.split(' ')
    answer = []
    for element in temp:
        answer.append(element.capitalize())
    return ' '.join(answer)
print(solution(input()))