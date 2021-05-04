k = int(input())
dA = [46] * 46
dB = [46] * 46
dA[0], dA[1] = 1, 0
dB[0], dB[1] = 0, 1
for i in range(2, k+1):
    dA[i] = dA[i-1] + dA[i-2]
    dB[i] = dB[i-1] + dB[i-2]
print(dA[k], dB[k])