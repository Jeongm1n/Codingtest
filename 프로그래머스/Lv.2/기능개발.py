def solution(progresses, speeds):
    answer = []
    while len(progresses) > 0:
        if progresses[0] >= 100:
            cnt = 0 
            while progresses[0] >= 100:
                cnt += 1
                progresses.pop(0)
                speeds.pop(0)
                if len(progresses) == 0:
                    break
            answer.append(cnt)
        progresses = [progresses[i]+speeds[i] for i in range(len(progresses))]
    return answer
progresses = list(map(int, input().split()))
speeds = list(map(int, input().split()))
print(solution(progresses, speeds))