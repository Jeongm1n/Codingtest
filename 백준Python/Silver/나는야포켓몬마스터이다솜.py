import sys

m, n = map(int, sys.stdin.readline().split())
pkmn = []
pkmn_dic = {}

for i in range(m):
    pk = sys.stdin.readline().rstrip()
    pkmn.append(pk)
    pkmn_dic[pk] = i + 1

for _ in range(n):
    search = sys.stdin.readline().rstrip()
    if search.isdigit():
        print(pkmn[int(search) - 1])
    else:
        print(pkmn_dic[search])
