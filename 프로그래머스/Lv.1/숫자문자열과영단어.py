alpha = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def solution(s):
    start = 0
    end = 1
    answer = ""
    while start < len(s):
        if s[start].isdigit():
            answer += s[start]
            start = end
            end += 1
            continue
        if s[start:end] in alpha:
            answer += str(alpha.index(s[start:end]))
            start = end
            end += 1
        else:
            end += 1
    return int(answer)


s = input()
print(solution(s))
