def solution(n):
    binary = format(n, 'b')
    binary_cnt = binary.count('1')
    n += 1
    while 1:
        temp = format(n, 'b')
        temp_cnt = temp.count('1')
        if binary_cnt == temp_cnt:
            return n
        n += 1
print(solution(int(input())))