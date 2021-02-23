from itertools import product
def solution(numbers, target):
    '''
    cnt = 0
    len_numbers = len(numbers)
    def operator(idx=0):
        if idx < len_numbers:
            numbers[idx] *= 1
            operator(idx+1)

            numbers[idx] *= -1
            operator(idx+1)
        elif sum(numbers) == target:
            nonlocal cnt
            cnt += 1
    operator()
    return cnt
    '''
    i = [(x, -x) for x in numbers]
    j = list(map(sum, product(*i)))
    return j.count(target)
numbers = list(map(int, input().split()))
target = int(input())
print(solution(numbers, target))