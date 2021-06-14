import sys

input = sys.stdin.readline

bridge_length, weight = map(int, input().split())
truck_weights = list(map(int, input().split()))


def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length
    time = 0
    while bridge:
        time += 1
        bridge.pop(0)
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    return time


print(solution(bridge_length, weight, truck_weights))
