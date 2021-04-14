n = int(input())
m = int(input())
dic = {}
for i in range(n):
    dic[i+1] = set()
for i in range(m):
    a, b = map(int, input().split())
    dic[a].add(b)
    dic[b].add(a)
    
def bfs(start, dic):
    queue = [start]
    while queue:
        for i in dic[queue.pop()]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
visited = []
bfs(1, dic)
print(len(visited)-1)