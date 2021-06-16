import sys
from collections import defaultdict

input = sys.stdin.readline

genres = list(map(str, input().split()))
plays = list(map(int, input().split()))


def solution(genres, plays):
    answer = []
    genresPlays = defaultdict(int)
    genresSongs = defaultdict(lambda: [])
    i = 0
    for g, p in zip(genres, plays):
        genresPlays[g] += p
        genresSongs[g].append((i, p))
        i += 1

    sortedGenres = sorted(genresPlays.items(), key=lambda x: x[1], reverse=True)

    for g in sortedGenres:
        sortedG = sorted(genresSongs[g[0]], key=lambda x: x[1], reverse=True)
        answer.append(sortedG[0][0])
        if len(sortedG) > 1:
            answer.append(sortedG[1][0])

    return answer


print(solution(genres, plays))
