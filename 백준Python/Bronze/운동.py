N, m, M, T, R = map(int, input().split())
current_pulse = m
time = 0
exerciese_time = 0
while 1:
    if (m + T) > M:
        time = -1
        break
    if (current_pulse + T) <= M:
        time += 1
        exerciese_time += 1
        current_pulse += T
    else:
        time += 1
        current_pulse -= R
        if current_pulse <= m:
            current_pulse = m
    if exerciese_time == N:
        break
print(time)