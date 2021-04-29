n = int(input())
for _ in range(n):
    string = list(input().split())
    Astr = list(string[0])
    Bstr = list(string[1])
    
    tempA = sorted(Astr)
    tempB = sorted(Bstr)
    if tempA == tempB:
        print('%s & %s are anagrams.' %(''.join(Astr), ''.join(Bstr)))
    else:
        print('%s & %s are NOT anagrams.' %(''.join(Astr), ''.join(Bstr)))