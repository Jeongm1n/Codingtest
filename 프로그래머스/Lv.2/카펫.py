def solution(brown, yellow):
    for i in range(1, yellow+1):
        if yellow % i == 0: # 가로 길이의 경우들 i
            temp = yellow // i # i에 맞는 세로 길이 temp
            if 2*i + 2*temp + 4 == brown: # 가로와 세로길이에 맞는 brown 확인
                return [temp+2, i+2]
brown = int(input())
yellow = int(input())
print(solution(brown, yellow))