def solution(s):
    answer = ''
    word = s.split(' ')
    for i in range(len(word)):
        for j in range(len(word[i])):
            if j%2==0:
                answer+=word[i][j].upper()
            else:
                answer+=word[i][j].lower()
        answer+=' '
    return answer[:-1]

a = "try hello world"
print(solution(a))