n = int(input())
call = list(map(int, input().split()))
y_cost = 0
m_cost = 0
for i in range(len(call)):
    y_cost += (call[i]//30) * 10 + 10
    m_cost += (call[i]//60) * 15 + 15

if y_cost > m_cost:
    print('M %d' % m_cost)
elif y_cost < m_cost:
    print('Y %d' % y_cost)
else:
    print('Y M %d' % y_cost)