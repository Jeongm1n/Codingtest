def solution(brown, yellow):
    for i in range(1, yellow+1):
        if yellow % i==0:  # 가로 길이의 경우들 i
            a = yellow // i  # i에 맞는 세로 길이 a
            if 2*i + 2*a + 4 == brown: # 가로와 세로길이에 맞는 brown 확인
                return [a+2, i+2]

brown = 24
yellow = 24
print(solution(brown, yellow))