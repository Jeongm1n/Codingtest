import sys
def fun(n, arr):
    for k in range(n, -1, -1):
        cnt = 0
        up = []
        for j in arr:
            if k <= j:
                cnt += 1
                up.append(j)
        if k <= cnt:
            set_arr = set(arr)
            set_up = set(up)
            set_down = set_arr - set_up
            if len(set_down) <= k:
                print(k)
                return
    print(0)
    return

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
fun(n, arr)