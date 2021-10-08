# def solution(param0):
#     graph = [[0] * 6 for _ in range(6)]

#     for i in range(0, len(param0), 3):
#         if param0[i] + param0[i + 2] > 6:
#             return []
#         if sum(graph[param0[i + 1]][param0[i] : param0[i] + param0[i + 2]]) > 0:
#             return []
#         for j in range(1, param0[i + 2] + 1):
#             graph[param0[i + 1]][param0[i] + j - 1] = j

#         for i in range(6):
#             temp = 0
#             for j in range(6):
#                 temp += graph[j][i]
#             if temp == 10:
#                 for k in range(6):
#                     graph[k][i] = 0
#     answer = []
#     for i in range(6):
#         temp_s = ""
#         for j in range(6):
#             if graph[i][j] == 0:
#                 temp_s += " "
#             else:
#                 temp_s += str(graph[i][j])
#         answer.append(temp_s)
#     return answer


# param0 = list(map(int, input().split()))
# print(solution(param0))


# def boost_bin2hex(value):
#     return hex(int(value, 2))


# def solution(param0):
#     reg = ["A", "B", "C", "D", "E", "H", "L"]
#     bit = ["111", "000", "001", "010", "011", "100", "101"]
#     if param0[:2] != "LD" and param0[:2] != "LN":
#         return "ERROR"
#     if param0[:2] == "LD":
#         if param0[3] not in reg or param0[5] not in reg:
#             return "ERROR"
#         elif param0[3] == param0[5]:
#             return "NOOP"
#     if param0[:2] == "LN":
#         if param0[5].isalpha():
#             return "ERROR"
#         else:
#             if int(param0[5:]) < 0 or int(param0[5:]) > 256:
#                 return "ERROR"

#     if param0[:2] == "LD":
#         temp = "0b01"
#         bit_value1 = bit[reg.index(param0[3])]
#         bit_value2 = bit[reg.index(param0[5])]

#         temp = temp + bit_value1 + bit_value2
#         answer = boost_bin2hex(temp)
#         answer = list(answer.upper())
#         answer[1] = "x"
#         return "".join(answer)


# param0 = input()
# print(solution(param0))
# from collections import deque

# m, n, k = map(int, input().split())
# graph = [[0] * n for _ in range(m)]
# for _ in range(k):
#     x1, y1, x2, y2 = map(int, input().split())
#     for i in range(x1, x2):
#         for j in range(m - y1 - 1, m - y2 - 1, -1):
#             graph[j][i] = 1

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]


# def bfs(x, y):
#     global answer
#     queue = deque()
#     queue.append((x, y))
#     graph[x][y] = 1
#     size = 1
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0:
#                 graph[nx][ny] = 1
#                 queue.append((nx, ny))
#                 size += 1
#     answer.append(size)


# answer = []
# for i in range(m):
#     for j in range(n):
#         if graph[i][j] == 0:
#             bfs(i, j)
# answer.sort()
# print(answer)

from collections import deque


def getTheGroups(n, queryType, student1, student2):
    graph = [[] for _ in range(n + 1)]
    for i in range(len(student1)):
        for j in range(len(student1)):
            if student1[i] != student1[j] and student1[j] not in graph[student1[i]]:
                graph[student1[i]].append(student1[j])
    for i in range(len(student2)):
        for j in range(len(student2)):
            if student2[i] != student2[j] and student2[j] not in graph[student2[i]]:
                graph[student2[i]].append(student2[j])
    if len(student1) == 1 and len(student2) == 1:
        return 2
    else:
        return bfs(1, n, graph)


def bfs(start, n, graph):
    queue = deque()
    queue.append(start)
    visited = [False] * (n + 1)
    visited[start] = True

    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)
    return visited.count(True)


print(getTheGroups(2, ["Friend", "Total"], [1], [2]))
