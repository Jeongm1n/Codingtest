from itertools import permutations
def solution(numbers):
    temp = set()
    for i in range(len(numbers)):
        temp |= set(map(int, map(''.join, permutations(list(numbers), i+1))))
    temp -= set(range(0, 2))
    for i in range(2, int(max(temp)**0.5)+1):
        temp -= set(range(i*2, max(temp)+1, i))
    return len(temp)
numbers = input()
print(solution(numbers))