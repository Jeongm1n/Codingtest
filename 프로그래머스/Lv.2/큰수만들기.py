def solution(number, k):
    collected = []
    for (i, num) in enumerate(number):
        while collected and collected[-1] < num and k > 0:
            collected.pop()
            k -= 1
        if k == 0:
            collected += number[i:]
            break
        collected.append(num)
    collected = collected[:-k] if k > 0 else collected
    return ''.join(collected)
number = input()
k = int(input())
print(solution(number, k))