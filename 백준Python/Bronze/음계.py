data = list(map(int, input().split()))
if data == sorted(data):
    print('ascending')
elif data == sorted(data, reverse=True):
    print('descending')
else:
    print('mixed')