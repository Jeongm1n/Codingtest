import collections
n = int(input())
data = list(map(int, input().split()))
count = collections.Counter(data)
print(max(count.values()))