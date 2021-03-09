n = int(input())
arr = list(map(int, input().split()))
temp = []
for _ in range(n):
    max_value = max(arr)
    min_value = min(arr)
    arr.remove(max_value)
    arr.remove(min_value)
    temp.append(max_value+min_value)
print(min(temp))