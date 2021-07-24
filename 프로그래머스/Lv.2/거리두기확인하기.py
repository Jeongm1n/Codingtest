from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j, length, element):
    q = deque()
    result = []
    visited = [[0] * length for _ in range(length)]
    visited[i][j] = 1
    q.append([i, j])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= length or ny >= length:
                continue
            if element[nx][ny] == "X":
                continue
            if (visited[nx][ny] == 0 and element[nx][ny] == "O") or (
                visited[nx][ny] == 0 and element[nx][ny] == "P"
            ):

                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])

                if element[nx][ny] == "P":
                    if visited[nx][ny] > 3:
                        result.append(1)
                    else:
                        result.append(0)
    if 0 in result:
        return False
    else:
        return True


def temp(element, length):
    tempResult = []
    for i in range(length):
        for j in range(length):
            if element[i][j] == "P":
                temp = bfs(i, j, length, element)
                if temp:
                    tempResult.append(1)
                else:
                    tempResult.append(0)
    if 0 in tempResult:
        return 0
    else:
        return 1


def solution(places):
    answer = []
    for i in places:
        answer.append(temp(i, len(places)))
    return answer


print(
    solution(
        [
            ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
            ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
            ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
            ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
            ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
        ]
    )
)
