n, l, d = map(int, input().split())
music_list = []
for i in range(n):
    for j in range(l):
        music_list.append(1)
    for k in range(5):
        music_list.append(0)
        
time = 0
while 1 :
    if time >= len(music_list):
        break
    if music_list[time] == 0:
        break
    else:
        time += d
        
print(time)