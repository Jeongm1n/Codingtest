from collections import Counter

def solution(clothes):
    counter_each_category = Counter([cat for _, cat in clothes])
    possible_cnt = 1
    
    for key in counter_each_category:
        possible_cnt *= (counter_each_category[key] + 1)
        # 각 종류의 수 +1하여 모두 곱하기
    return possible_cnt - 1

clothes=[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"],["fu", "leg"]]
print(solution(clothes))