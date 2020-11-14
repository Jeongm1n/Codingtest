# H를 입력받기
h = int(input())

count= 0

# 시, 분, 초를 알아야하므로 3중 반복문 사용
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있으면 count 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1
                
print(count)