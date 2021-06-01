import sys

input = sys.stdin.readline
numbers = list(map(int, input().split()))
hand = input()


def solution(numbers, hand):
    lastL, lastR = 10, 12
    answer = ""
    for n in numbers:
        if n in [1, 4, 7]:
            lastL = n
            answer += "L"
        elif n in [3, 6, 9]:
            lastR = n
            answer += "R"
        else:
            n = 11 if n == 0 else n
            absL = abs(n - lastL)
            absR = abs(n - lastR)
            if sum(divmod(absL, 3)) > sum(divmod(absR, 3)):
                lastR = n
                answer += "R"
            elif sum(divmod(absL, 3)) < sum(divmod(absR, 3)):
                lastL = n
                answer += "L"
            else:
                if hand == "left":
                    lastL = n
                    answer += "L"
                else:
                    lastR = n
                    answer += "R"
    return answer


print(solution(numbers, hand))
