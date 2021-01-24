def solution(arr):
    answer = []
    idx = arr.index(min(arr))
    answer = arr
    del answer[idx]
    if not answer:
        answer.append(-1)
    return answer
