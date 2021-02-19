def solution(bridge_length, weight, truck_weights):
    time = 0
    temp = [0] * bridge_length
    while temp:
        time += 1
        temp.pop(0)
        if truck_weights:
            if sum(temp) + truck_weights[0] <= weight:
                temp.append(truck_weights.pop(0))
            else:
                temp.append(0)
    return time
bridge_length = int(input())
weight = int(input())
truck_weights = list(map(int, input().split()))
print(solution(bridge_length, weight, truck_weights))