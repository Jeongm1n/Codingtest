def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i]+numbers[j])
    
    return sorted(list(set(answer)))

numbers = [1,2,3,4,5]
print(solution(numbers))
  
  
