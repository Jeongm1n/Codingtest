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
    from itertools import product   
    i = [(x, -x) for x in numbers]
    j = list(map(sum, product(*i)))
    return j.count(target)
    
numbers=[1,1,1,1,1]
target=3
print(solution(numbers, target))