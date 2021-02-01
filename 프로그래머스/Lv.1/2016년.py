def solution(a, b):
    day = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = b
    if a != 1:
        for i in range(a-1):
            total += month[i]
    return day[total%7]
a, b = map(int, input().split())
print(solution(a, b))