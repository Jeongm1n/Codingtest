def solution(n):
    answer = []
    number = str(n)
    for i in range(len(number)-1, -1, -1):
        answer.append(int(number[i]))
    return answer
n = int(input())
print(solution(n))