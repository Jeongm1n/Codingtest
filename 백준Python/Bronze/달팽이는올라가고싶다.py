# a, b, v = map(int, input().split())
# print((v-b-1)//(a-b)+1)
a, b, v = map(int, input().split())
k = (v-b)/(a-b) # 정상에 도달한 이후, 밤에 미끄러지 않는 것을 반영 v-b
print(int(k) if k == int(k) else int(k)+1)