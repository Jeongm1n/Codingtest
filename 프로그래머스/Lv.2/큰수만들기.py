def solution(number, k):
    collected = []  # 숫자를 모아 큰 수를 만들 때 쓰는 배열
    
    for i, num in enumerate(number): # enumerate는 인덱스 확인
        # k개만큼의 숫자를 빼냈을 때, i의 인덱스를 기억하기 위해 i 사용
        while len(collected) > 0 and collected[-1] < num and k > 0:
            # 
            collected.pop()
            k-=1
        if k==0:
            collected += list(number[i:])
            break
        collected.append(num)
    collected = collected[:-k] if k > 0 else collected
    
    answer = ''.join(collected)
    return answer

number = "4177252841"
k = 4
print(solution(number, k))