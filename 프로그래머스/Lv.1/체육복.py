def solution(n, lost, reserve):
    # 여벌 체육복에 관한 경우 적용
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    return n-len(set_lost)
n = int(input())
lost = list(map(int, input().split()))
reserve = list(map(int, input().split()))
print(solution(n, lost, reserve))