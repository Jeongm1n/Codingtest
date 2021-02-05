def solution(answers):
    answer_a = [1, 2, 3, 4, 5]
    answer_b = [2, 1, 2, 3, 2, 4, 2, 5]
    answer_c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == answer_a[i%len(answer_a)]:
            score[0] += 1
        if answers[i] == answer_b[i%len(answer_b)]:
            score[1] += 1
        if answers[i] == answer_c[i%len(answer_c)]:
            score[2] += 1
    result = []
    biggest_score = max(score)
    result.append(score.index(max(score))+1)
    for i in range(3):
        if i == score.index(max(score)):
            continue
        if score[i] == biggest_score:
            result.append(i+1)
    return result
answers = list(map(int, input().split()))
print(solution(answers))