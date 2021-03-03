arr = []
for _ in range(9):
    num = int(input())
    arr.append(num)
print(max(arr), arr.index(max(arr))+1, sep='\n')