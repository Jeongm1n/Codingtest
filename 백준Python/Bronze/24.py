h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))
t = 0
while not(h1 == h2 and m1 == m2 and s1 == s2):
    s1 += 1
    t += 1
    if s1 == 60:
        s1 = 0
        m1 += 1
        if m1 == 60:
            m1 = 0
            h1 += 1
            if h1 == 24:
                h1 = 0
s = t%60
m = (t//60) % 60
h = (t//60) // 60
print(f'{h:0>2}:{m:0>2}:{s:0>2}')