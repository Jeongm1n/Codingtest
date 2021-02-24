while 1:
    arr = list(map(int, input().split()))
    if sum(arr) == 0:
        break
    biggest_value = max(arr)
    arr.remove(biggest_value)
    if (arr[0]**2)+(arr[1]**2) == biggest_value**2:
        print('right')
    else:
        print('wrong')