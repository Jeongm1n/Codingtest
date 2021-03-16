import sys
n = int(sys.stdin.readline())
answer = [int(sys.stdin.readline()) for _ in range(n)]
answer.sort()
for num in answer:
    print(num)