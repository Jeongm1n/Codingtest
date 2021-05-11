def solution(N, stages):
    answer = {} # dictionary를 이용해 {"stage_numer": 실패율}로 처리
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            answer[stage] = count / denominator
            denominator -= count
        else:
            answer[stage] = 0
    return sorted(answer, key=lambda x : answer[x], reverse=True)

n = int(input())
stages = list(map(int, input().split()))
print(solution(n, stages))