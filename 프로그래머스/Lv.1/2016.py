def solution(a, b):
    answer = ''
    total = 0
    day = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    for i in range(13):
        if i==a:
            for j in range(i-1):
                total += month[j]
    total = total + b
    total = total % 7
    for i in range(7):
        if total == i:
            answer = day[i]
    return answer

a=int(input())
b=int(input())
print(solution(a,b))