def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:x*3, reverse=True)
    print(numbers)
    return str(int(''.join(numbers)))

numbers=[3,30,34,5,9]
print(solution(numbers))